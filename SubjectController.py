from utils import  validate_email,validate_password
from Subject import Subject

def subject_controller(db, student):
    students = db.load_students()  
    while True:
        print("\n=== Subject Enrolment System ===")
        print("(c) change password")
        print("(e) enrol")
        print("(r) remove")
        print("(s) show subjects")
        print("(x) exit")
        choice = input("Select an option: ").lower()

        if choice == 'c':
            new_pass = input("New Password: ")
            if not validate_password(new_pass):
                print("Invalid password format.")
                continue
            student.password = new_pass
            db.save_students(students)
            print("Password updated.")
        elif choice == 'e':
            if len(student.subjects) >= 4:
                print("Cannot enroll in more than 4 subjects.")
            else:
                new_subject = Subject()
                student.enroll_subject(new_subject)
                db.save_students(students)
                print(f"Enrolled in subject {new_subject.id} with mark {new_subject.mark}, grade {new_subject.grade}.")
        elif choice == 'r':
            subject_id = input("Enter subject ID to remove: ")
            student.remove_subject(subject_id)
            db.save_students(students)
            print("Subject removed.")
        elif choice == 's':
            if not student.subjects:
                print("No subjects enrolled.")
            else:
                for subj in student.subjects:
                    print(f"ID: {subj.id}, Mark: {subj.mark}, Grade: {subj.grade}")
                print(f"Average: {student.calculate_average():.2f}, Pass: {student.is_pass()}")
        elif choice == 'x':
            break
        else:
            print("Invalid option.")
