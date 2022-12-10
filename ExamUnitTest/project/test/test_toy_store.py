from project.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):
    def test_init(self):
        store = ToyStore()
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, store.toy_shelf)

    def test_add_toy_if_shelf_not_in_collection_raise(self):
        store = ToyStore()
        with self.assertRaises(Exception) as ex:
            store.add_toy("H", "Toy")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))
        self.assertEqual({"A": None, "B": None, "C": None, "D": None, "E": None, "F": None, "G": None, }, store.toy_shelf)

    def test_add_toy_if_toy_in_shelf_raise(self):
        store = ToyStore()
        store.toy_shelf = {"A": "Toy", "B": None, "C": None, "D": None, "E": None, "F": None, "G": None, }
        with self.assertRaises(Exception) as ex:
            store.add_toy("A", "Toy")
        self.assertEqual("Toy is already in shelf!", str(ex.exception))
        self.assertEqual({"A": "Toy", "B": None, "C": None, "D": None, "E": None, "F": None, "G": None, }, store.toy_shelf)

    def test_add_toy_if_toy_in_shelf_is_not_None_raise(self):
        store = ToyStore()
        store.toy_shelf = {"A": "Toy", "B": None, "C": None, "D": None, "E": None, "F": None, "G": None, }
        with self.assertRaises(Exception) as ex:
            store.add_toy("A", "Test")
        self.assertEqual("Shelf is already taken!", str(ex.exception))
        self.assertEqual({"A": "Toy", "B": None, "C": None, "D": None, "E": None, "F": None, "G": None, }, store.toy_shelf)

    def test_add_toy_correct_data(self):
        store = ToyStore()
        store.toy_shelf = {"A": None, "B": None, "C": None, "D": None, "E": None, "F": None, "G": None, }
        result = store.add_toy("A", "Toy1")
        expected = f"Toy:Toy1 placed successfully!"
        self.assertEqual(expected, result)
        self.assertEqual({"A": "Toy1", "B": None, "C": None, "D": None, "E": None, "F": None, "G": None, }, store.toy_shelf)
        result = store.add_toy("B", "Toy2")
        expected = f"Toy:Toy2 placed successfully!"
        self.assertEqual(expected, result)
        self.assertEqual({"A": "Toy1", "B": "Toy2", "C": None, "D": None, "E": None, "F": None, "G": None, }, store.toy_shelf)

    def test_remove_toy_if_shelf_not_in_collection_raise(self):
        store = ToyStore()
        store.toy_shelf = {"A": "Toy1", "B": "Toy2", "C": None, "D": None, "E": None, "F": None, "G": None, }
        with self.assertRaises(Exception) as ex:
            store.remove_toy("H", "Toy")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))
        self.assertEqual({"A": "Toy1", "B": "Toy2", "C": None, "D": None, "E": None, "F": None, "G": None, }, store.toy_shelf)

    def test_remove_toy_if_toy_name_not_correct_raise(self):
        store = ToyStore()
        store.toy_shelf = {"A": "Toy1", "B": "Toy2", "C": None, "D": None, "E": None, "F": None, "G": None, }
        with self.assertRaises(Exception) as ex:
            store.remove_toy("A", "Toy")
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))
        self.assertEqual({"A": "Toy1", "B": "Toy2", "C": None, "D": None, "E": None, "F": None, "G": None, }, store.toy_shelf)

    def test_remove_toy_correct_data(self):
        store = ToyStore()
        store.toy_shelf = {"A": "Toy1", "B": "Toy2", "C": None, "D": None, "E": None, "F": None, "G": None, }
        result = store.remove_toy("A", "Toy1")
        expected = f"Remove toy:Toy1 successfully!"
        self.assertEqual(expected, result)
        self.assertEqual({"A": None, "B": "Toy2", "C": None, "D": None, "E": None, "F": None, "G": None, }, store.toy_shelf)
        result = store.remove_toy("B", "Toy2")
        expected = f"Remove toy:Toy2 successfully!"
        self.assertEqual(expected, result)
        self.assertEqual({"A": None, "B": None, "C": None, "D": None, "E": None, "F": None, "G": None, },
                         store.toy_shelf)


if __name__ == "__main__":
    main()
