from database import create_table
from yoobee_manager import add_record, delete_record, view_all_records

def menu():
    print("       Student Management System")
    print("1. Add Record")
    print("2. Delete Record")
    print("3. View All Records")
    print("4. Exit")

def get_table_choice():
    print("\nChoose table to operate on:")
    print("1. Student")
    print("2. Teacher")
    print("3. Course")
    print("4. Class")
    try:
        choice = int(input("Please choose (1-4): "))
        tables = {1: "Student", 2: "Teacher", 3: "Course", 4: "Class"}
        return tables.get(choice)
    except ValueError:
        print("Please enter a valid number!")
        return None

def add_record_interactive():
    """Interactive add record"""
    table_name = get_table_choice()
    if not table_name:
        return

    print(f"\nAdd {table_name} record:")

    if table_name == "Student":
        student_number = int(input("Student Number: "))
        name = input("Name: ")
        gender = input("Gender: ")
        date_of_birth = input("Date of Birth (year-month-day): ")
        nationality = input("Nationality: ")
        data = (student_number, name, gender, date_of_birth, nationality)

    elif table_name == "Teacher":
        job_number = int(input("Job Number: "))
        name = input("Name: ")
        gender = input("Gender: ")
        date_of_birth = input("Date of Birth (year-month-day): ")
        major = input("Major: ")
        data = (job_number, name, gender, date_of_birth, major)

    elif table_name == "Course":
        course_id = int(input("Course ID: "))
        name = input("Course Name: ")
        hours = int(input("Hours: "))
        data = (course_id, name, hours)

    elif table_name == "Class":
        class_id = int(input("Class ID: "))
        name = input("Class Name: ")
        number_of_people = int(input("Number of People: "))
        data = (class_id, name, number_of_people)

    add_record(table_name, data)

def delete_record_interactive():
    table_name = get_table_choice()
    if not table_name:
        return
    record_id = int(input(f"Please enter the ID of the {table_name} record to delete: "))
    delete_record(table_name, record_id)

def view_all_records_interactive():
    table_name = get_table_choice()
    if not table_name:
        return

    records = view_all_records(table_name)
    if records:
        print(f"\n {table_name} Records")
        for record in records:
            print(record)
    else:
        print(f"No {table_name} records found!")

def main():
    create_table()

    while True:
        menu()

        try:
            choice = int(input("Please choose operation (1-4): "))

            if choice == 1:
                add_record_interactive()
            elif choice == 2:
                delete_record_interactive()
            elif choice == 3:
                view_all_records_interactive()
            elif choice == 4:
                print("Thank you for using Student Management System!")
                break
            else:
                print("Invalid choice, please try again!")

        except ValueError:
            print("Error: Please enter a valid number!")

if __name__ == "__main__":
    main()