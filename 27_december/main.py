import tkinter as tk
from tkinter import filedialog
from openpyxl import load_workbook
from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

dsn = {
    "dbname": os.environ.get("POSTGRES_DB"),
    "host": os.environ.get("POSTGRES_HOST"),
    "port": os.environ.get("POSTGRES_PORT"),
    "user": os.environ.get("POSTGRES_USER"),
    "password": os.environ.get("POSTGRES_PASSWORD"),
}

def create_matrix_from_file(file_path: str) -> list:
    wb = load_workbook(file_path)
    ws = wb.active
    matrix = []

    for row in ws:
        matrix.append([cell.value for cell in row])

    for row in matrix:
        for cell_value in row:
            print(cell_value, end='\t\t')
        print()

    return matrix


def on_proceed_button_click():
    try:
        file_path = file_path_entry.get()
        matrix = create_matrix_from_file(file_path) # Наша матрица
        with psycopg2.connect(**dsn) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS test_1(
                        id SERIAL NOT NULL PRIMARY KEY,
                        title TEXT NOT NULL,
                        description TEXT NOT NULL,
                        success BOOLEAN NOT NULL,
                        deadline DATE NOT NULL,
                        date_created DATE NOT NULL
                    );
                    """
                )
                for row in matrix[1:]:
                    cur.execute(
                        """
                        INSERT INTO test_1 VALUES (%s, %s, %s, %s, %s, %s);
                        """,
                        row
                    )
    except Exception as e:
        print(e)


def on_browse_button_click():
    file_path = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title="Select Excel file",
        filetypes=[("Excel files", "*.xlsx")]
    )
    file_path_entry.delete(0, tk.END)
    file_path_entry.insert(0, file_path)


root = tk.Tk()

file_path_label = tk.Label(text="Enter the file path: ")
file_path_entry = tk.Entry(width=20)
browse_button = tk.Button(
    width=20,
    text="Browse...",
    command=on_browse_button_click
)

proceed_button = tk.Button(
    width=20,
    bg='black',
    fg='white',
    text="Proceed",
    command=on_proceed_button_click
)

file_path_label.grid(row=1, column=1, columnspan=2)
file_path_entry.grid(row=2, column=1)
browse_button.grid(row=2, column=2)
proceed_button.grid(row=3, column=1, columnspan=2)

root.mainloop()
