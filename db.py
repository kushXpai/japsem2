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

def insert_user(conn, name, email):
    try:
        with conn:
            conn.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
            print("User inserted.")
    except sqlite3.IntegrityError:
        print("Error: Email must be unique.")
    except sqlite3.Error as e:
        print("Insert Error:", e)

def fetch_users(conn):
    try:
        cur = conn.cursor()
        cur.execute('SELECT * FROM users')
        users = cur.fetchall()
        for user in users:
            print("User:", user)
    except sqlite3.Error as e:
        print("Read Error:", e)

def update_user_email(conn, user_id, new_email):
    try:
        with conn:
            conn.execute('UPDATE users SET email = ? WHERE id = ?', (new_email, user_id))
            print("User updated.")
    except sqlite3.Error as e:
        print("Update Error:", e)

def delete_user(conn, user_id):
    try:
        with conn:
            conn.execute('DELETE FROM users WHERE id = ?', (user_id,))
            print("User deleted.")
    except sqlite3.Error as e:
        print("Delete Error:", e)

def close_db(conn):
    if conn:
        conn.close()

conn = connect_db()
if conn:
    create_table(conn)
    insert_user(conn, "Alice", "alice@example.com")
    insert_user(conn, "Bob", "bob@example.com")
    fetch_users(conn)
    update_user_email(conn, 1, "alice_new@example.com")
    delete_user(conn, 2)
    fetch_users(conn)
    close_db(conn)