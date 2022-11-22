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
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Basic", "new_note")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_if_course_name_in_courses(self):
        result = self.student.leave_course("web")
        self.assertEqual("Course has been removed", result)
        self.assertFalse("web" in self.student.courses)
        self.assertTrue(len(self.student.courses) > 0)

    def test_leave_course_if_course_not_in_courses(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Basic")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))











if __name__ == "__main__":
    main()
