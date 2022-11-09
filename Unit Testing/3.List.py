class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)

from unittest import TestCase, main


class Test(TestCase):

    def test_initializing_integerscorrectly(self):
        list_ = IntegerList(4, 5)
        self.assertEqual([4, 5], list_._IntegerList__data)

    def test_initializing_not_integerscorrectly(self):
        list_ = IntegerList("abc", 3.5)
        self.assertEqual([], list_._IntegerList__data)

    def test_initializing_correctly_with_empty_list(self):
        list_ = IntegerList([])
        self.assertEqual([], list_._IntegerList__data)

    def test_get_data(self):
        list_ = IntegerList(4, 5, "asd")
        result = list_.get_data()
        self.assertEqual([4, 5], result)

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
        list_.remove_index(1)
        self.assertEqual(2, len(list_._IntegerList__data))
        self.assertEqual([1, 3], list_._IntegerList__data)

    def test_remove_index_with_correct_index(self):
        list_ = IntegerList(1, 2, 3)
        result = list_.remove_index(1)
        self.assertEqual(2, result)

    def test_remove_index_with_incorrect_index(self):
        list_ = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError) as ex:
            list_.remove_index(4)
        self.assertEqual("Index is out of range", str(ex.exception))
        with self.assertRaises(IndexError) as ex:
            list_.remove_index(3)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_index_with_incorrect_index(self):
        list_ = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError) as ex:
            list_.get(5)
        self.assertEqual("Index is out of range", str(ex.exception))
        with self.assertRaises(IndexError) as ex:
            list_.get(3)
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


if __name__ == "__main__":
    main()
