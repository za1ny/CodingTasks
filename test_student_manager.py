# test_student_manager.py class testing
import unittest
from student_manager import Student, StudentManager


class TestStudent(unittest.TestCase):

    def setUp(self):
        # Add a new student in list / Arrange
        self.student = Student(0, "Adam", "Brown")

    def test_add_grade(self):
        # Test if add_grade method correctly adds a grade
        self.student.add_grade("English", 80)
        # Assert - seeing if the values correspond
        self.assertEqual(self.student.grades, {"English": 80})

    def test_grade_average(self):
        # Test if grade_average correctly averages multiple grades
        self.student.add_grade("English", 80)
        self.student.add_grade("Maths", 83)
        self.student.add_grade("Science", 77)
        # Act - seeing if the values are correct
        result = self.student.grade_average()
        # Assert - confirming average grade is 80
        self.assertEqual(result, 80)


class TestStudentManager(unittest.TestCase):

    def setUp(self) -> None:
        self.student_manager = StudentManager()

    def test_add_student(self):
        # Test to see if adding student is correctly done
        new_student = Student(1, "Amy", "Yellow")
        self.student_manager.add_student(new_student)
        self.assertListEqual(self.student_manager.student, [new_student])
