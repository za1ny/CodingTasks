# student_manager.py
class TodoList:

    def __init__(self):
        # Initialise an empty list to store tasks
        self.tasks = []

    def add_task(self, task):
        # Add a new task to the list
        self.tasks.append(task)

    def update_task(self, old_task, new_task):
        # Update an existing task in the list
        if old_task in self.tasks:
            index = self.tasks.index(old_task)
            self.tasks[index] = new_task

    def remove_task(self, task):
        # Remove a task from the list
        if task in self.tasks:
            self.tasks.remove(task)


class StudentManager:

    def __init__(self):
        # Initialise an empty list to store students
        self.students = []

    def add_student(self, student):
        # Add a new student to the list
        self.students.append(student)

    def get_student(self, id):
        # Retrieves student name in list
        for student in self.student:
            if student.id == id:
                return student

    def remove_student(self, id):
        # Remove a student from the list
        for i in range(len(self.students)):
            if self.student[i].id == id:
                del self.students[i]