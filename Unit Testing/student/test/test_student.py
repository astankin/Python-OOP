from unittest import TestCase, main

from project.student import Student


class StudentTest(TestCase):
    def setUp(self) -> None:
        courses = {
            "web": ["note1", "note2"],
            "oop": ["note3", "note4"]
        }
        self.student = Student("Test", courses)

    def test_student_init(self):
        student = Student("Test")
        self.assertEqual("Test", student.name)
        self.assertEqual({}, student.courses)

    def test_init_with_courses(self):
        courses = {
            "web": ["note1", "note2"],
            "oop": ["note3", "note4"]
        }
        student = Student("Test", courses)
        self.assertEqual("Test", student.name)
        self.assertEqual(courses, student.courses)

    def test_enroll_course_name_in_courses(self):
        result = self.student.enroll("web", ["note5"])
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual(["note1", "note2", "note5"], self.student.courses["web"])

    def test_enroll_add_course_notes_Y_value(self):
        result = self.student.enroll("Basic", ["new_notes"], "Y")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(self.student.courses["Basic"], ["new_notes"])

    def test_enroll_add_course_notes_no_value(self):
        result = self.student.enroll("Basic", ["new_notes"], "")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(["new_notes"], self.student.courses["Basic"])

    def test_enroll_course(self):
        result = self.student.enroll("Basic", ["notes5"], "N")
        self.assertEqual("Course has been added.", result)
        self.assertTrue("Basic" in self.student.courses)
        self.assertEqual([], self.student.courses["Basic"])

    def test_add_notes_to_existing_notes(self):
        result = self.student.add_notes("web", "new_note")
        self.assertEqual("Notes have been updated", result)
        self.assertEqual(["note1", "note2", "new_note"], self.student.courses["web"])

    def test_add_notes_to_not_existing_notes_raises(self):









if __name__ == "__main__":
    main()
