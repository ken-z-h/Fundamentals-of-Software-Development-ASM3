def admin_menu(db):
    students = db.load_students()
    while True:
        print("\n=== Admin System ===")
        print("(c) clear database")
        print("(g) group students by grade")
        print("(p) partition students PASS/FAIL")
        print("(r) remove student by ID")
        print("(s) show all students")
        print("(x) exit")
        choice = input("Select an option: ").lower()

        if choice == 'c':
            confirm = input("Are you sure? (yes/no): ")
            if confirm.lower() == 'yes':
                db.clear_data()
                print("Database cleared.")
        elif choice == 'g':
            grades = {}
            for s in students:
                for subj in s.subjects:
                    grades.setdefault(subj.grade, []).append((s.name, subj.id))
            for grade, lst in grades.items():
                print(f"Grade {grade}: {lst}")
        elif choice == 'p':
            pass_list = [s.name for s in students if s.is_pass()]
            fail_list = [s.name for s in students if not s.is_pass()]
            print(f"PASS: {pass_list}")
            print(f"FAIL: {fail_list}")
        elif choice == 'r':
            sid = input("Enter student ID to remove: ")
            students = [s for s in students if s.id != sid]
            db.save_students(students)
            print("Student removed.")
        elif choice == 's':
            for s in students:
                print(f"ID: {s.id}, Name: {s.name}, Email: {s.email}, Subjects: {[subj.id for subj in s.subjects]}")
        elif choice == 'x':
            break
        else:
            print("Invalid option.")
