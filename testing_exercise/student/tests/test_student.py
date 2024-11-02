from project.student import Student
from unittest import TestCase, main


class TestStudent(TestCase):

    def setUp(self):
        self.student = Student("Test", courses=None)
        self.student_two = Student("Test2", {"Python-OOP": ["Advanced"], "JS": ["React"]})

    def test_init(self):
        self.assertEqual("Test", self.student.name)
        self.assertEqual("Test2", self.student_two.name)
        self.assertEqual({}, self.student.courses)
        self.assertEqual({"Python-OOP": ["Advanced"], "JS": ["React"]}, self.student_two.courses)

    def test_enroll_with_available_course(self):
        self.assertEqual("Course already added. Notes have been updated.",
                         self.student_two.enroll("Python-OOP", ["aa", "bb"]))
        self.assertEqual({"Python-OOP": ["Advanced", "aa", "bb"], "JS": ["React"]}, self.student_two.courses)

    def test_enroll_with_empty_notes(self):
        self.assertEqual("Course and course notes have been added.",
                         self.student.enroll("Python-OOP", ["Advanced"], ""))
        self.assertEqual({"Python-OOP": ["Advanced"]}, self.student.courses)

    def test_enroll_with_Y(self):
        self.assertEqual("Course and course notes have been added.", self.student.enroll("Python-OOP", ["Advanced"], "Y"))
        self.assertEqual({"Python-OOP": ["Advanced"]}, self.student.courses)

    def test_enrol_with_other_notes(self):
        self.assertEqual("Course has been added.", self.student.enroll("Python", ["aa", "bb"], "aaa"))
        self.assertEqual({"Python": []}, self.student.courses)

    def test_add_notes(self):
        with self.assertRaises(Exception) as s:
            self.student.add_notes("JS-basics", ["ab", "bb"])
        self.assertEqual("Cannot add notes. Course not found.", str(s.exception))

        self.assertEqual("Notes have been updated", self.student_two.add_notes("JS", "cc"))
        self.assertEqual({"Python-OOP": ["Advanced"], "JS": ["React", "cc"]}, self.student_two.courses)

    def test_leave_course(self):
        with self.assertRaises(Exception) as s:
            self.student.leave_course("JS")
        self.assertEqual("Cannot remove course. Course not found.", str(s.exception))

        self.assertEqual("Course has been removed", self.student_two.leave_course("Python-OOP"))
        self.assertEqual({"JS": ["React"]}, self.student_two.courses)


if __name__ == "__main__":
    main()