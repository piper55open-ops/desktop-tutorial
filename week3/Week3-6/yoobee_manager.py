import sqlite3
from database import create_connection


def add_record(table_name, data):
    conn = create_connection()
    cursor = conn.cursor()

    try:
        if table_name == "Student":
            cursor.execute('''
                INSERT INTO Student (student_number, name, gender, date_of_birth, nationality)
                VALUES (?, ?, ?, ?, ?)
            ''', data)
        elif table_name == "Teacher":
            cursor.execute('''
                INSERT INTO Teacher (job_number, name, gender, date_of_birth, major)
                VALUES (?, ?, ?, ?, ?)
            ''', data)
        elif table_name == "Course":
            cursor.execute('''
                INSERT INTO Course (course_id, name, hours)
                VALUES (?, ?, ?)
            ''', data)
        elif table_name == "Class":
            cursor.execute('''
                INSERT INTO Class (class_id, name, number_of_people)
                VALUES (?, ?, ?)
            ''', data)
        else:
            print("invaild！")
            return False

        conn.commit()
        print(f"{table_name} success！")
        return True

    except sqlite3.IntegrityError:
        print("error！")
        return False
    except sqlite3.Error as e:
        print(f"error: {e}")
        return False
    finally:
        conn.close()


def delete_record(table_name, record_id):
    conn = create_connection()
    cursor = conn.cursor()

    try:
        if table_name == "Student":
            id_field = "student_number"
        elif table_name == "Teacher":
            id_field = "job_number"
        elif table_name == "Course":
            id_field = "course_id"
        elif table_name == "Class":
            id_field = "class_id"
        else:
            print("error")
            return False

        cursor.execute(f'DELETE FROM {table_name} WHERE {id_field} = ?', (record_id,))
        conn.commit()

        if cursor.rowcount > 0:
            print(f"{table_name} success！")
            return True
        else:
            print("none！")
            return False

    except sqlite3.Error as e:
        print(f"error: {e}")
        return False
    finally:
        conn.close()


def view_all_records(table_name):
    conn = create_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(f"SELECT * FROM {table_name}")
        records = cursor.fetchall()
        return records
    except sqlite3.Error as e:
        print(f"error: {e}")
        return []
    finally:
        conn.close()
