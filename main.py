import json

FILE_NAME = "students.json"


# Calculate grade based on marks
def calculate_grade(marks):
    if 80 <= marks <= 100:
        return "A"
    elif 70 <= marks <= 79:
        return "B"
    elif 60 <= marks <= 69:
        return "C"
    elif 50 <= marks <= 59:
        return "D"
    else:
        return "F"


# Load data from JSON file
def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            loaded_students = {}
            updated = False

            for student_id, details in data.items():
                sid = int(student_id)
                if "grade" not in details:
                    details["grade"] = calculate_grade(details["marks"])
                    updated = True
                loaded_students[sid] = details

            if updated:
                with open(FILE_NAME, "w") as out_file:
                    json.dump(loaded_students, out_file, indent=4)

            return loaded_students
    except (FileNotFoundError, json.JSONDecodeError, ValueError):
        return {}


# Save data to JSON file
def save_data():
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


# Load existing records when program starts
students = load_data()


def add_student():
    print("\n--- Add Student ---")

    # Validate numeric Student ID
    while True:
        try:
            student_id = int(input("Enter student ID: "))
            break
        except ValueError:
            print("Invalid input! Please enter numbers only for Student ID.")

    if student_id in students:
        print("Student ID already exists!")
    else:
        name = input("Enter student name: ")

        # Validate numeric marks (0 to 100)
        while True:
            try:
                marks = int(input("Enter student marks (0-100): "))
                if 0 <= marks <= 100:
                    break
                else:
                    print("Invalid marks! Please enter a value between 0 and 100.")
            except ValueError:
                print("Invalid input! Please enter numbers only.")

        grade = calculate_grade(marks)

        students[student_id] = {
            "name": name,
            "marks": marks,
            "grade": grade
        }
        save_data()
        print("Student added successfully!")


def view_students():
    if not students:
        print("\nNo student records available.")
    else:
        print("\n--- All Students Record ---\n")
        for student_id, details in students.items():
            print(f"ID: {student_id} | Name: {details['name']} | Marks: {details['marks']} | Grade: {details['grade']}")


def search_student():
    print("\n--- Search Student ---\n")

    # Validate numeric Student ID
    while True:
        try:
            search_id = int(input("Enter student ID: "))
            break
        except ValueError:
            print("Invalid input! Please enter numbers only for Student ID.")

    if search_id in students:
        details = students[search_id]
        print("\nStudent Found!")
        print(f"ID: {search_id}")
        print(f"Name: {details['name']}")
        print(f"Marks: {details['marks']}")
        print(f"Grade: {details['grade']}")
    else:
        print("Student not found!")


def update_student():
    print("\n--- Update Student ---")

    # Validate numeric Student ID
    while True:
        try:
            update_id = int(input("Enter student ID: "))
            break
        except ValueError:
            print("Invalid input! Please enter numbers only for Student ID.")

    if update_id in students:
        print(f"Current Marks: {students[update_id]['marks']}")

        # Validate numeric marks (0 to 100)
        while True:
            try:
                new_marks = int(input("Enter new marks (0-100): "))
                if 0 <= new_marks <= 100:
                    break
                else:
                    print("Invalid marks! Please enter a value between 0 and 100.")
            except ValueError:
                print("Invalid input! Please enter numbers only.")

        students[update_id]["marks"] = new_marks
        students[update_id]["grade"] = calculate_grade(new_marks)
        save_data()
        print("Student marks updated successfully!")
    else:
        print("Student not found!")


def delete_student():
    print("\n--- Delete Student ---")

    # Validate numeric Student ID
    while True:
        try:
            delete_id = int(input("Enter student ID: "))
            break
        except ValueError:
            print("Invalid input! Please enter numbers only for Student ID.")

    if delete_id in students:
        del students[delete_id]
        save_data()
        print(f"Student with ID {delete_id} deleted successfully!")
    else:
        print("Student not found!")


# Main Menu Loop
while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====\n")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit\n")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Exiting Student Management System. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 6.")