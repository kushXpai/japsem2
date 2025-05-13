import sqlite3

def connect_db(db_name='test.db'):
    try:
        return sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print("Connection Error:", e)
        return None

def fetch_users(conn):
    try:
        cur = conn.cursor()
        cur.execute('SELECT * FROM users')
        users = cur.fetchall()
        for user in users:
            print("User:", user)
    except sqlite3.Error as e:
        print("Read Error:", e)

def close_db(conn):
    if conn:
        conn.close()

conn = connect_db()
if conn:
    fetch_users(conn)
    close_db(conn)