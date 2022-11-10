from project.unittest import TestCase

from list import IntegerList


class Test(TestCase):

    def test_initializing_correctly(self):
        list_ = IntegerList(1, "abc", 3.5, 5)
        self.assertEqual([1, 5], list_._IntegerList__data)

    def test_add_operation_adding_integer_and_returning_a_list(self):
        list_ = IntegerList(1, 2)
        list_.add(3)
        self.assertEqual([1, 2, 3], list_._IntegerList__data)

    def test_add_operation_adding_non_integer_raises(self):
        list_ = IntegerList(1, 2)
        with self.assertRaises(ValueError) as ex:
            list_.add("3")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_remove_index_with_correct_index_and_return_the_value(self):
        list_ = IntegerList(1, 2, 3)
        result = list_.remove_index(1)
        self.assertEqual(2, result)

    def test_remove_index_with_correct_index(self):
        list_ = IntegerList(1, 2, 3)
        result = list_.remove_index(1)
        self.assertEqual(2, len(list_._IntegerList__data))

    def test_remove_index_with_incorrect_index(self):
        list_ = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError) as ex:
            list_.remove_index(4)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_index_with_incorrect_index(self):
        list_ = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError) as ex:
            list_.get(5)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_index(self):
        list_ = IntegerList(1, 2, 3)
        result = list_.get(2)
        self.assertEqual(3, result)

    def test_insert_with_index_out_of_range_raises(self):
        list_ = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError) as ex:
            list_.insert(5, 4)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_element_which_is_not_integer(self):
        list_ = IntegerList(1, 2, 3)
        with self.assertRaises(ValueError) as ex:
            list_.insert(1, "4")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_get_biggest_element(self):
        list_ = IntegerList(100, 5, 25, -132, 46)
        result = list_.get_biggest()
        self.assertEqual(100, result)

    def test_get_index_of_element(self):
        list_ = IntegerList(100, 5, 25, 132, 46)
        result = list_.get_index(25)
        self.assertEqual(2, result)
