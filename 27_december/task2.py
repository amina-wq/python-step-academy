from dotenv import load_dotenv
import os
import psycopg2
from faker import Faker

load_dotenv()
fake = Faker()

dsn = {
    "dbname": os.environ.get("POSTGRES_DB"),
    "host": os.environ.get("POSTGRES_HOST"),
    "port": os.environ.get("POSTGRES_PORT"),
    "user": os.environ.get("POSTGRES_USER"),
    "password": os.environ.get("POSTGRES_PASSWORD")
}

def init_db(conn: psycopg2.extensions.connection) -> None:
    with conn.cursor() as cur:
        cur.execute(
                """
                CREATE TABLE IF NOT EXISTS table_1(
                    id SERIAL NOT NULL PRIMARY KEY,
                    last_name VARCHAR(30) NOT NULL,
                    first_name VARCHAR(30) NOT NULL,
                    city VARCHAR(30) NOT NULL,
                    address VARCHAR(100) NOT NULL
                );
                """
        )

def insert_data(conn: psycopg2.extensions.connection) -> None:
    with conn.cursor() as cur:
        for _ in range(10000):
            query = cur.mogrify(
                f"""
                INSERT INTO table_1 VALUES(
                    default,
                    '{fake.last_name()}',
                    '{fake.first_name()}',
                    '{fake.city()}',
                    '{fake.address()}'
                );
                """
            )
            cur.execute(query)

def get_data(conn: psycopg2.extensions.connection) -> None:
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT * FROM table_1;
            """
        )
        for row in cur.fetchall():
            print(row)

def update(conn: psycopg2.extensions.connection) -> None:
    with conn.cursor() as cur:
        cur.execute(
            """
            UPDATE table_1 
            SET last_name='Zhuravkov'
            Where last_name='Davis';
            """
        )

if __name__ == "__main__":
    with psycopg2.connect(**dsn) as conn:
        #init_db(conn)
        #insert_data(conn)
        #get_data(conn)
        update(conn)