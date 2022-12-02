from unittest import TestCase, main

from project.student_report_card import StudentReportCard


class TestStudentReportCart(TestCase):
    def test_init(self):
        cart = StudentReportCard("Test", 2)
        self.assertEqual("Test", cart.student_name)
        self.assertEqual(2, cart.school_year)
        self.assertEqual({}, cart.grades_by_subject)

    def test_name_empty_string_raise(self):
        with self.assertRaises(ValueError) as ve:
            cart = StudentReportCard("", 12)
        self.assertEqual("Student Name cannot be an empty string!", str(ve.exception))
        with self.assertRaises(ValueError) as ve:
            cart = StudentReportCard("", 1)
        self.assertEqual("Student Name cannot be an empty string!", str(ve.exception))

    def test_school_year_raise(self):
        with self.assertRaises(ValueError) as ve:
            cart = StudentReportCard("Testt", 0)
        self.assertEqual("School Year must be between 1 and 12!", str(ve.exception))
        with self.assertRaises(ValueError) as ve:
            cart = StudentReportCard("Testt", 13)
        self.assertEqual("School Year must be between 1 and 12!", str(ve.exception))

    def test_add_grade(self):
        cart = StudentReportCard("Testt", 10)
        cart.add_grade("Math", 5.5)
        self.assertEqual({"Math": [5.5]}, cart.grades_by_subject)
        cart.add_grade("Math", 4.5)
        self.assertEqual({"Math": [5.5, 4.5]}, cart.grades_by_subject)
        cart.add_grade("Math", 0)
        self.assertEqual({"Math": [5.5, 4.5, 0]}, cart.grades_by_subject)
        self.assertEqual(len(cart.grades_by_subject), 1)

    def test_average_grade_by_subject(self):
        cart = StudentReportCard("Testt", 10)
        result = cart.average_grade_by_subject()
        expected = ""
        self.assertEqual(expected, result)
        cart.add_grade("Math", 5.5)
        cart.add_grade("Math", 4.5)
        cart.add_grade("English", 4.5)
        cart.add_grade("English", 4.5)
        result = cart.average_grade_by_subject()
        expected = f"Math: 5.00\n" \
                   f"English: 4.50"
        self.assertEqual(expected, result)

    def test_average_grade_for_all_subjects(self):
        cart = StudentReportCard("Testt", 10)
        cart.add_grade("Math", 5.5)
        cart.add_grade("Math", 4.5)
        cart.add_grade("English", 4.5)
        cart.add_grade("English", 4.5)
        result = cart.average_grade_for_all_subjects()
        expected = f"Average Grade: 4.75"
        self.assertEqual(expected, result)

    def test_repr(self):
        cart = StudentReportCard("Test", 10)
        cart.add_grade("Math", 5.5)
        cart.add_grade("Math", 4.5)
        cart.add_grade("English", 4.5)
        cart.add_grade("English", 4.5)
        expected = f"Name: Test\n" \
                   f"Year: 10\n" \
                   f"----------\n" \
                   f"Math: 5.00\n" \
                   f"English: 4.50\n" \
                   f"----------\n" \
                   f"Average Grade: 4.75"

        self.assertEqual(expected, repr(cart))


if __name__ == "__main__":
    main()
