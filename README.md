# University Application - CLI & GUI

A software project developed in Python to simulate a university application system with **command-line interface (CLI)** and a  GUIUniApp.

This project was developed as part of Assessment 1 - Part 2 at University of Technology Sydney (UTS).

---

## 📋 Features

### CLIUniApp (Command Line Interface)
- Register a new student (email & password validation)
- Login for registered students
- Enrol in up to 4 subjects
- Remove enrolled subjects
- Change password
- View enrolled subjects with marks & grades
- Admin features:
  - View all students
  - Remove student by ID
  - Clear all student data
  - Partition students as PASS/FAIL
  - Group students by grade

All data is stored in a local file `students.data` using Python's `pickle` module.

---

### GUIUniApp (PyQt5 GUI Application)

⚠️ **The GUI implementation is currently under development.**

Planned features:
- Login window
- Enrolment window (max 4 subjects)
- Subjects window (display marks and grades)
- Exception dialogs (invalid login, over-enrolment, etc.)

GUI will use the same `students.data` file as CLI.

---

## 🛠️ Installation

1. Clone or download this repository
1. Activate virtual environment:

- Windows:

  ```bash
  venv\Scripts\activate
  ```

- macOS/Linux:

  ```bash
  source venv/bin/activate
  ```

------

## 🚀 Running the application

### Running CLI

```bash
python app.py
```

### Running GUI

⚠️ **GUI will be available in a future version.**

------

## 📁 Project Structure

```
Fundamentals-of-Software-Development-ASM3/
├── AdminMenu.py            # Admin menu logic
├── app.py                  # Main CLI entry point
├── Database.py             # Database file handling
├── Student.py              # Student class (model)
├── StudentController.py     # Student controller functions
├── Subject.py              # Subject class (model)
├── SubjectController.py     # Subject controller functions
├── utils.py                # Validation helper functions
├── students.data           # Data file (generated after first run)
└──  README.md
```

------

## ✅ Valid Email Format

- Must follow pattern: `firstname.lastname@university.com`
  - Example: `john.doe@university.com`

## ✅ Valid Password Format

- Starts with uppercase letter
- At least 5 letters total
- Ends with at least 3 digits
  - Example: `Aabcd123`

------

## 📝 Notes

- Data file `students.data` will be automatically created if missing.
- Ensure you run CLI/GUI from the same directory to access `students.data`.

------

## 👨‍👩‍👧‍👦 Contributions

This project was developed by **Group**  as part of **Assessment 1 - Part 2 & 3**.

Each team member contributed to coding, testing, and presentation.

------

## 🏫 University of Technology Sydney

Faculty of Engineering and IT – Assessment 1