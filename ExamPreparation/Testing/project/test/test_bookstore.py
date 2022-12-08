from project.bookstore import Bookstore
from unittest import TestCase, main

class TestBookstore(TestCase):
    def test_init(self):
        store = Bookstore(100)
        self.assertEqual(100, store.books_limit)
        self.assertEqual({}, store.availability_in_store_by_book_titles)
        self.assertEqual(0, store.total_sold_books)

    def test_init_book_limit_raise(self):
        with self.assertRaises(ValueError) as ve:
            store = Bookstore(0)
        expected = f"Books limit of 0 is not valid"
        self.assertEqual(expected, str(ve.exception))
        with self.assertRaises(ValueError) as ve:
            store = Bookstore(-15)
        expected = f"Books limit of -15 is not valid"
        self.assertEqual(expected, str(ve.exception))

    def test_len(self):
        store = Bookstore(100)
        store.availability_in_store_by_book_titles = {"Book1": 5, "Book2": 5}
        self.assertEqual(10, len(store))

    def test_receive_book_raise(self):
        store = Bookstore(10)
        store.availability_in_store_by_book_titles = {"Book1": 5, "Book2": 5}
        with self.assertRaises(Exception) as ex:
            store.receive_book("Book3", 5)
        expected = "Books limit is reached. Cannot receive more books!"
        self.assertEqual(expected, str(ex.exception))
        self.assertEqual({"Book1": 5, "Book2": 5}, store.availability_in_store_by_book_titles)

    def test_receive_book(self):
        store = Bookstore(20)
        store.availability_in_store_by_book_titles = {"Book1": 5, "Book2": 5}
        result = store.receive_book("Book3", 5)
        expected = f"5 copies of Book3 are available in the bookstore."
        self.assertEqual(expected, result)
        self.assertEqual({"Book1": 5, "Book2": 5, "Book3": 5}, store.availability_in_store_by_book_titles)
        result = store.receive_book("Book3", 5)
        expected = f"10 copies of Book3 are available in the bookstore."
        self.assertEqual(expected, result)
        self.assertEqual({"Book1": 5, "Book2": 5, "Book3": 10}, store.availability_in_store_by_book_titles)

    def test_sell_book_if_title_not_in_collection_raise(self):
        store = Bookstore(20)
        store.availability_in_store_by_book_titles = {"Book1": 5, "Book2": 5}
        with self.assertRaises(Exception) as ex:
            store.sell_book("Book4", 5)
        expected = f"Book Book4 doesn't exist!"
        self.assertEqual(expected, str(ex.exception))
        self.assertEqual(10, len(store))

    def test_sell_book_if_quantity_not_enough(self):
        store = Bookstore(20)
        store.availability_in_store_by_book_titles = {"Book1": 5, "Book2": 5}
        with self.assertRaises(Exception) as ex:
            store.sell_book("Book2", 6)
        expected = f"Book2 has not enough copies to sell. Left: 5"
        self.assertEqual(expected, str(ex.exception))
        self.assertEqual(10, len(store))

    def test_sell_book_correct_data(self):
        store = Bookstore(20)
        store.availability_in_store_by_book_titles = {"Book1": 5, "Book2": 5}
        result = store.sell_book("Book2", 5)
        expected = f"Sold 5 copies of Book2"
        self.assertEqual(expected, result)
        self.assertEqual(5, len(store))
        self.assertEqual({"Book1": 5, "Book2": 0}, store.availability_in_store_by_book_titles)
        self.assertEqual(5, store.total_sold_books)

        result = store.sell_book("Book1", 2)
        expected = f"Sold 2 copies of Book1"
        self.assertEqual(expected, result)
        self.assertEqual(3, len(store))
        self.assertEqual({"Book1": 3, "Book2": 0}, store.availability_in_store_by_book_titles)
        self.assertEqual(7, store.total_sold_books)

    def test_str(self):
        store = Bookstore(20)
        store.availability_in_store_by_book_titles = {"Book1": 5, "Book2": 5}
        store.sell_book("Book2", 3)
        result = f"Total sold books: 3\n" \
                 f"Current availability: 7\n" \
                 f" - Book1: 5 copies\n" \
                 f" - Book2: 2 copies"
        self.assertEqual(result, str(store))

if __name__ == "__main__":
    main()