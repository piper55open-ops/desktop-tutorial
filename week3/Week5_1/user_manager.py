from database import create_connection
import sqlite3

def add_user(name, email):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        print(" User added successfully.")
    except sqlite3.IntegrityError:
        print(" Email must be unique.")
    conn.close()

def view_users():
    conn = create_connection()
    cursor = conn.cursor()
    print(" User.")
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_user(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_user(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    print("🗑️ User deleted.")

def insert_sample_students():
    conn = create_connection()
    cursor = conn.cursor()
    sample_students = [
        (1, 'lijiuyu', 'henan'),
        (2, 'dingding', 'fugou')
    ]

    cursor.executemany('''
    INSERT OR IGNORE INTO student (Stu_ID, Stu_name, Stu_address)
    VALUES (?, ?, ?)
    ''', sample_students)

    conn.commit()
    conn.close()

def get_all_students():
    print(" student.")
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student")
    students = cursor.fetchall()
    conn.close()
    return students