
from SubjectController import subject_menu
from Student import Student
from utils import  validate_email,validate_password

def student_controller(db):
    students = db.load_students()
    while True:
        print("\n=== Student System ===")
        print("(l) login")
        print("(r) register")
        print("(x) exit")
        choice = input("Select an option: ").lower()

        if choice == 'l':
            email = input("Email: ")
            password = input("Password: ")
            student = next((s for s in students if s.email == email and s.password == password), None)
            if student:
                print(f"Welcome {student.name}!")
                subject_menu(db, student)
            else:
                print("Invalid credentials.")
        elif choice == 'r':
            name = input("Name: ")
            email = input("Email: ")
            if not validate_email(email):
                print("Invalid email format.")
                continue
            if any(s.email == email for s in students):
                print("Email already registered.")
                continue
            password = input("Password: ")
            if not validate_password(password):
                print("Invalid password format.")
                continue
            new_student = Student(name, email, password)
            students.append(new_student)
            db.save_students(students)
            print("Registration successful.")
        elif choice == 'x':
            break
        else:
            print("Invalid option.")
