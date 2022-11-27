from project.bookstore import Bookstore
from unittest import TestCase, main


class TestBookStore(TestCase):

    def test_init(self):
        store = Bookstore(100)
        self.assertEqual(100, store.books_limit)
        self.assertEqual({}, store.availability_in_store_by_book_titles)
        self.assertEqual(0, store.total_sold_books)

    def test_books_limit_equal_to_zero_raises(self):
        with self.assertRaises(ValueError) as er:
            store = Bookstore(0)
        self.assertEqual("Books limit of 0 is not valid", str(er.exception))

    def test_books_limit_negative_value_raises(self):
        with self.assertRaises(ValueError) as er:
            store = Bookstore(-10)
        self.assertEqual("Books limit of -10 is not valid", str(er.exception))

    def test_count_books(self):
        store = Bookstore(100)
        store.availability_in_store_by_book_titles = {"Test1": 2, "Test2": 3}
        self.assertEqual(5, len(store))

    def test_receive_book_if_enough_capacity_and_book_not_in_collection(self):
        store = Bookstore(100)
        result = store.receive_book("Test1", 50)
        self.assertEqual(f"50 copies of Test1 are available in the bookstore.", result)
        self.assertEqual(50, len(store))

    def test_receive_book_if_enough_capacity_and_book_in_collection(self):
        store = Bookstore(100)
        store.receive_book("Test1", 50)
        result = store.receive_book("Test1", 50)
        self.assertEqual(f"100 copies of Test1 are available in the bookstore.", result)
        self.assertEqual(100, len(store))

    def test_receive_book_if_not_enough_capacity_raises(self):
        store = Bookstore(10)
        with self.assertRaises(Exception) as ex:
            store.receive_book("Test1", 50)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_sell_book_if_book_not_in_collection_raise(self):
        store = Bookstore(100)
        store.receive_book("Test1", 10)
        with self.assertRaises(Exception) as ex:
            store.sell_book("Test2", 50)
        self.assertEqual("Book Test2 doesn't exist!", str(ex.exception))

    def test_sell_book_if_not_enough_quantity_raise(self):
        store = Bookstore(100)
        store.receive_book("Test1", 10)
        with self.assertRaises(Exception) as ex:
            store.sell_book("Test1", 50)
        self.assertEqual("Test1 has not enough copies to sell. Left: 10", str(ex.exception))

    def test_sell_book_with_correct_data(self):
        store = Bookstore(100)
        store.receive_book("Test1", 30)
        result1 = store.sell_book("Test1", 30)
        self.assertEqual("Sold 30 copies of Test1", result1)
        self.assertEqual(0, len(store))
        self.assertEqual(30, store.total_sold_books)

    def test_str_(self):
        store = Bookstore(100)
        store.receive_book("Test1", 30)
        store.receive_book("Test2", 20)
        store.sell_book("Test1", 10)
        result = str(store)
        self.assertEqual(f"Total sold books: 10\n"
                         f"Current availability: 40\n"
                         f" - Test1: 20 copies\n"
                         f" - Test2: 20 copies", result)


if __name__ == "__main__":
    main()
