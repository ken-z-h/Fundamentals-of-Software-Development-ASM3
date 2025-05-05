import random

class Subject:
    def __init__(self, id=None, mark=None):
        self.id = id if id else str(random.randint(1, 999)).zfill(3)
        self.mark = mark if mark else random.randint(25, 100)
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.mark >= 85:
            return 'HD'
        elif self.mark >= 75:
            return 'D'
        elif self.mark >= 65:
            return 'C'
        elif self.mark >= 50:
            return 'P'
        else:
            return 'F'