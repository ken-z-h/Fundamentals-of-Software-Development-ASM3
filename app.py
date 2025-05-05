from AdminMenu import admin_menu
from Database import Database
from StudentController import student_menu
def main_menu():
    db = Database()
    while True:
        print("\n=== University System ===")
        print("(A) Admin")
        print("(S) Student")
        print("(X) Exit")
        choice = input("Select an option: ").upper()

        if choice == 'A':
            admin_menu(db)
        elif choice == 'S':
            student_menu(db)
        elif choice == 'X':
            print("Exiting program.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main_menu()