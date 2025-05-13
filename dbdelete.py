import sqlite3

def connect_db(db_name='test.db'):
    try:
        return sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print("Connection Error:", e)
        return None

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
    delete_user(conn, 2)
    close_db(conn)