from project.library import Library
from unittest import TestCase, main


class TestLibrary(TestCase):
    def test_init(self):
        test = Library("Test")
        self.assertEqual("Test", test.name)
        self.assertEqual({}, test.books_by_authors)
        self.assertEqual({}, test.readers)

    def test_init_name_an_empty_string_raise(self):
        with self.assertRaises(ValueError) as err:
            test = Library("")
        self.assertEqual("Name cannot be empty string!", str(err.exception))

    def test_add_books_author_and_title_not_in_collection(self):
        test = Library("Test")
        test.add_book("Author", "Title")
        self.assertEqual({"Author": ["Title"]}, test.books_by_authors)
        test.add_book("Author", "Title2")
        self.assertEqual({"Author": ["Title", "Title2"]}, test.books_by_authors)
        test.add_book("Author", "Title2")
        self.assertEqual({"Author": ["Title", "Title2"]}, test.books_by_authors)

    def test_add_reader_name_not_in_collection(self):
        test = Library("Test")
        test.add_reader("Reader")
        self.assertEqual({"Reader": []}, test.readers)

    def test_add_reader_name_already_in_collection(self):
        test = Library("Test")
        test.add_reader("Reader")
        result = test.add_reader("Reader")
        self.assertEqual(f"Reader is already registered in the Test library.", result)

    def test_rent_book_reader_not_in_readers(self):
        test = Library("Test")
        test.add_book("Author", "Title")
        result = test.rent_book("Reader", "Author", "Title")
        self.assertEqual(f"Reader is not registered in the Test Library.", result)
        self.assertEqual({}, test.readers)

    def test_rent_book_author_not_in_collection(self):
        test = Library("Test")
        test.add_book("Author", "Title")
        test.add_reader("Reader")
        result = test.rent_book("Reader", "Author1", "Title")
        self.assertEqual(f"Test Library does not have any Author1's books.", result)
        result = test.rent_book("Reader", "Author", "Title1")
        self.assertEqual(f"""Test Library does not have Author's "Title1".""", result)

    def test_rent_book_correct_data(self):
        test = Library("Test")
        test.add_book("Author", "Title")
        test.add_reader("Reader")
        test.rent_book("Reader", "Author", "Title")
        self.assertEqual({"Reader": [{"Author": "Title"}]}, test.readers)
        self.assertEqual({"Author": []}, test.books_by_authors)





if __name__ == "__main__":
    main()
