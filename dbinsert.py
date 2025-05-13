import sqlite3

def connect_db(db_name='test.db'):
    try:
        return sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print("Connection Error:", e)
        return None

def insert_user(conn, name, email):
    try:
        with conn:
            conn.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
            print("User inserted.")
    except sqlite3.IntegrityError:
        print("Error: Email must be unique.")
    except sqlite3.Error as e:
        print("Insert Error:", e)

def close_db(conn):
    if conn:
        conn.close()

conn = connect_db()
if conn:
    insert_user(conn, "Alice", "alice@example.com")
    insert_user(conn, "Bob", "bob@example.com")
    close_db(conn)