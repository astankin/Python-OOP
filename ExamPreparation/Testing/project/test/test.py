from unittest import TestCase, main

from project.library import Library


class TestLibrary(TestCase):
    def test_init(self):
        test = Library("Test")
        self.assertEqual("Test", test.name)
        self.assertEqual({}, test.books_by_authors)
        self.assertEqual({}, test.readers)

    def test_init_raise(self):
        with self.assertRaises(ValueError) as ve:
            test = Library("")
        self.assertEqual("Name cannot be empty string!", str(ve.exception))

    def test_add_book(self):
        test = Library("Test")
        test.add_book("Author", "Title")
        self.assertEqual({"Author": ["Title"]}, test.books_by_authors)
        test.add_book("Author", "Title1")
        self.assertEqual({"Author": ["Title", "Title1"]}, test.books_by_authors)
        test.add_book("Author", "Title1")
        self.assertEqual({"Author": ["Title", "Title1"]}, test.books_by_authors)

    def test_add_reader(self):
        test = Library("Test")
        test.add_reader("Reader")
        self.assertEqual({"Reader": []}, test.readers)
        result = test.add_reader("Reader")
        self.assertEqual(f"Reader is already registered in the Test library.", result)

    def test_rent_rent_book_incorrect_data(self):
        test = Library("Test")
        test.add_book("Author", "Title")
        result = test.rent_book("Reader", "Author", "Title")
        self.assertEqual(f"Reader is not registered in the Test Library.", result)
        test.add_reader("Reader")
        result = test.rent_book("Reader", "Author1", "Title")
        self.assertEqual(f"Test Library does not have any Author1's books.", result)
        result = test.rent_book("Reader", "Author", "Title1")
        self.assertEqual(f"""Test Library does not have Author's "Title1".""", result)

    def test_rent_book_correct_data(self):
        test = Library("Test")
        test.add_book("Author", "Title1")
        test.add_book("Author", "Title2")
        test.add_reader("Reader")
        test.rent_book("Reader", "Author", "Title1")
        self.assertEqual({"Reader": [{"Author": "Title1"}]}, test.readers)
        self.assertEqual({"Author": ["Title2"]}, test.books_by_authors)


if __name__ == "__main__":
    main()
