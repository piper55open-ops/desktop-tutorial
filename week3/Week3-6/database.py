import sqlite3


def create_connection():
    conn = sqlite3.connect("yoobee.db")
    return conn


def create_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Student (
            student_number INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            gender TEXT,
            date_of_birth TEXT,
            nationality TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Teacher (
            job_number INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            gender TEXT,
            date_of_birth TEXT,
            major TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Course (
            course_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            hours INTEGER
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Class (
            class_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            number_of_people INTEGER
        )
    ''')

    conn.commit()
    conn.close()