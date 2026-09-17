# Student Record Management System
# Course Project for Python Essentials

import os

FILE_NAME = "students_data.txt"

def load_students():
    students = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 4:
                    students.append({
                        "roll": parts[0],
                        "name": parts[1],
                        "course": parts[2],
                        "marks": parts[3]
                    })
    return students

def save_students(students):
    with open(FILE_NAME, "w") as file:
        for s in students:
            file.write(f"{s['roll']},{s['name']},{s['course']},{s['marks']}\n")

def add_student(students):
    print("\n--- Add New Student ---")
    roll = input("Enter Roll Number: ").strip()
    
    for s in students:
        if s['roll'] == roll:
            print("Student with this Roll Number already exists!")
            return

    name = input("Enter Name: ").strip()
    course = input("Enter Course: ").strip()
    marks = input("Enter Marks: ").strip()

    students.append({"roll": roll, "name": name, "course": course, "marks": marks})
    save_students(students)
    print("Student record added successfully!")

def view_students(students):
    print("\n--- Student Records ---")
    if not students:
        print("No student records found.")
        return

    print(f"{'Roll No':<10} | {'Name':<20} | {'Course':<15} | {'Marks':<10}")
    print("-" * 60)
    for s in students:
        print(f"{s['roll']:<10} | {s['name']:<20} | {s['course']:<15} | {s['marks']:<10}")

def search_student(students):
    print("\n--- Search Student ---")
    roll = input("Enter Roll Number to search: ").strip()
    found = False
    for s in students:
        if s['roll'] == roll:
            print("\nRecord Found:")
            print(f"Roll No : {s['roll']}")
            print(f"Name    : {s['name']}")
            print(f"Course  : {s['course']}")
            print(f"Marks   : {s['marks']}")
            found = True
            break
    if not found:
        print("Student not found.")

def main():
    students = load_students()
    while True:
        print("\n==================================")
        print(" STUDENT RECORD MANAGEMENT SYSTEM ")
        print("==================================")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            add_student(students)
        elif choice == '2':
            view_students(students)
        elif choice == '3':
            search_student(students)
        elif choice == '4':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
