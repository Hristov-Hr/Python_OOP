from project.senior_student import SeniorStudent

from unittest import TestCase, main

class TestSeniorStudent(TestCase):

    def setUp(self) -> None:
        self.student = SeniorStudent("1234", "Peter", 5.50)

    def test__init__(self):
        self.assertEqual("1234", self.student.student_id)
        self.assertEqual("Peter", self.student.name)
        self.assertEqual(5.50, self.student.student_gpa)
        self.assertEqual(set(), self.student.colleges)

    def test_student_id(self):
        with self.assertRaises(ValueError) as s:
            self.student.student_id = "123"
        self.assertEqual("Student ID must be at least 4 digits long!", str(s.exception))

        with self.assertRaises(ValueError) as s:
            self.student.student_id = " 123 "
        self.assertEqual("Student ID must be at least 4 digits long!", str(s.exception))

    def test_name(self):
        with self.assertRaises(ValueError) as s:
            self.student.name = "     "
        self.assertEqual("Student name cannot be null or empty!", str(s.exception))

        self.student.name = "p"
        self.assertEqual("p", self.student.name)

    def test_student_gpa(self):
        with self.assertRaises(ValueError) as s:
            self.student.student_gpa = 1.0
        self.assertEqual("Student GPA must be more than 1.0!", str(s.exception))
        self.student.student_gpa = 1.1
        self.assertEqual(1.1, self.student.student_gpa)

    def test_apply_to_college(self):
        self.assertEqual('Application failed!', self.student.apply_to_college(5.6, "test"))
        self.assertEqual(set(), self.student.colleges)
        self.assertEqual('Peter successfully applied to Test.', self.student.apply_to_college(5.5, "Test"))
        self.assertEqual({"TEST"}, self.student.colleges)
        self.assertEqual('Peter successfully applied to test.', self.student.apply_to_college(5.5, "test"))
        self.assertEqual({"TEST"}, self.student.colleges)
        self.assertEqual('Peter successfully applied to test2.', self.student.apply_to_college(5.5, "test2"))
        self.assertEqual({"TEST", "TEST2"}, self.student.colleges)

    def test_update_gpa(self):
        self.assertEqual('The GPA has not been changed!', self.student.update_gpa(1.0))
        self.assertEqual(self.student.student_gpa, 5.50)
        self.assertEqual('Student GPA was successfully updated.', self.student.update_gpa(1.1))
        self.assertEqual(self.student.student_gpa, 1.1)

    def test__eq__(self):
        other = SeniorStudent("2222", "Ivan", 5.5)
        self.assertEqual(True, self.student.__eq__(other))

        other.student_gpa += 0.1
        self.assertEqual(False, self.student.__eq__(other))


if __name__ == "__main__":
    main()