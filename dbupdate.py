import sqlite3

def connect_db(db_name='test.db'):
    try:
        return sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print("Connection Error:", e)
        return None

def update_user_email(conn, user_id, new_email):
    try:
        with conn:
            conn.execute('UPDATE users SET email = ? WHERE id = ?', (new_email, user_id))
            print("User updated.")
    except sqlite3.Error as e:
        print("Update Error:", e)

def close_db(conn):
    if conn:
        conn.close()

conn = connect_db()
if conn:
    update_user_email(conn, 1, "alice_new@example.com")
    close_db(conn)