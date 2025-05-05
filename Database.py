import os
import pickle

class Database:
    FILE_NAME = 'students.data'

    def __init__(self):
        if not os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, 'wb') as f:
                pickle.dump([], f)  # initialize empty list

    def load_students(self):
        with open(self.FILE_NAME, 'rb') as f:
            return pickle.load(f)

    def save_students(self, students):
        with open(self.FILE_NAME, 'wb') as f:
            pickle.dump(students, f)

    def clear_data(self):
        with open(self.FILE_NAME, 'wb') as f:
            pickle.dump([], f)
