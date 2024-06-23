class StudentManager:

    def __init__(self):
        # Initialise an empty list to store students
        self.student = []

    def add_student(self, student):
        # Add a new student to the list
        self.student.append(student)

    def get_student(self, id):
        # Retrieves student name in list
        for student in self.student:
            if student.id == id:
                return student

    def remove_student(self, id):
        # Remove a student from the list
        for i in range(len(self.student)):
            if self.student[i].id == id:
                del self.student[i]


class Student:

    def __init__(self, id, name, surname, address=""):
        self.id = id
        self.name = name
        self.surname = surname
        self.address = address
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def grade_average(self):
        grade_total = 0
        for grade in self.grades.values():
            grade_total += grade
        return grade_total/len(self.grades)
