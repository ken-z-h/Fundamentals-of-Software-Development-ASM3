import random

class Student:
    def __init__(self, name, email, password, id=None, subjects=None):
        self.id = id if id else str(random.randint(1, 999999)).zfill(6)
        self.name = name
        self.email = email
        self.password = password
        self.subjects = subjects if subjects else []  # list of Subject objects

    def enroll_subject(self, subject):
        if len(self.subjects) >= 4:
            print("Exceed maximum number of subjects(4)")
        else:
            self.subjects.append(subject)

    def remove_subject(self, subject_id):
        self.subjects = [s for s in self.subjects if s.id != subject_id]

    def calculate_average(self):
        if not self.subjects:
            return 0
        return sum(s.mark for s in self.subjects) / len(self.subjects)

    def is_pass(self):
        return self.calculate_average() >= 50
