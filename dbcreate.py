import sqlite3

def connect_db(db_name='test.db'):
    try:
        return sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print("Connection Error:", e)
        return None

def create_table(conn):
    try:
        with conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL
                )
            ''')
            print("Table created.")
    except sqlite3.Error as e:
        print("Create Table Error:", e)

def close_db(conn):
    if conn:
        conn.close()

conn = connect_db()
if conn:
    create_table(conn)
    close_db(conn)