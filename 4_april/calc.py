import tkinter as tk


BUTTON_WIDTH = 4
BUTTON_HEIGHT = 2


def evaluate_expression():
    try:
        expression = entry.get()
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


def button_click(event):
    text = event.widget.cget("text")

    if text == "=":
        evaluate_expression()
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "⌫":
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current_text[:-1])
    else:
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current_text + text)


def init_buttons(buttons_list: list, start_row: int):
    col_val = 0
    for button in buttons_list:
        btn = tk.Button(app, text=button, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, font=('Arial', 20))
        btn.grid(row=start_row, column=col_val)
        btn.bind("<Button-1>", button_click)
        col_val += 1
        if col_val > 3:
            col_val = 0
            start_row += 1


if __name__ == '__main__':

    app = tk.Tk()
    app.title("Simple Calculator")

    entry = tk.Entry(app, width=20, font=('Arial', 20))
    entry.grid(row=0, column=0, columnspan=4)

    top_buttons = [
        '⌫', 'C'
    ]

    buttons = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', '.', '=', '+'
    ]

    init_buttons(top_buttons, 1)
    init_buttons(buttons, 2)

    app.mainloop()
