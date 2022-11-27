from project.plantation import Plantation
from unittest import TestCase, main


class TestPlantation(TestCase):
    def test_init(self):
        plant = Plantation(100)
        self.assertEqual(100, plant.size)
        self.assertEqual({}, plant.plants)
        self.assertEqual([], plant.workers)

    def test_size_negative_value_raise(self):
        with self.assertRaises(ValueError) as er:
            plant = Plantation(-10)
        self.assertEqual("Size must be positive number!", str(er.exception))

    def test_hire_worker_if_worker_not_in_collection(self):
        plant = Plantation(100)
        result = plant.hire_worker("Test")
        self.assertEqual(f"Test successfully hired.", result)
        self.assertEqual(["Test"], plant.workers)

    def test_hire_worker_worker_in_workers_raise(self):
        plant = Plantation(100)
        plant.hire_worker("Test")
        with self.assertRaises(ValueError) as er:
            plant.hire_worker("Test")
        self.assertEqual("Worker already hired!", str(er.exception))
        self.assertEqual(["Test"], plant.workers)

    def test_len(self):
        plant = Plantation(100)
        plant.plants = {"Test1": [1, 2, 3], "Test2": [1, 2]}
        self.assertEqual(5, len(plant))

    def test_planting_worker_in_plants(self):
        plant = Plantation(100)
        plant.hire_worker("Test_worker")
        plant.plants = {"Test_worker": ["1", "2", "3"], "Test2": ["1", "2"]}
        result = plant.planting("Test_worker", "4")
        self.assertEqual(f"Test_worker planted 4.", result)
        self.assertEqual(["1", "2", "3", "4"], plant.plants["Test_worker"])
        self.assertEqual(6, len(plant))

    def test_planting_worker_not_in_plants(self):
        plant = Plantation(100)
        plant.hire_worker("Test_worker")
        plant.plants = {"Test1": ["1", "2", "3"], "Test2": ["1", "2"]}
        result = plant.planting("Test_worker", "4")
        self.assertEqual(f"Test_worker planted it's first 4.", result)
        self.assertEqual(6, len(plant))
        self.assertEqual({"Test1": ["1", "2", "3"], "Test2": ["1", "2"], "Test_worker": ["4"]}, plant.plants)

    def test_planting_worker_not_in_workers_raise(self):
        plant = Plantation(100)
        plant.plants = {"Test1": ["1", "2", "3"], "Test2": ["1", "2"]}
        with self.assertRaises(ValueError) as err:
            plant.planting("Test", "4")
        self.assertEqual(f"Worker with name Test is not hired!", str(err.exception))

    def test_planting_if_bigger_of_size(self):
        plant = Plantation(3)
        plant.hire_worker("Test")
        plant.plants = {"Test1": ["1", "2", "3"], "Test2": ["1", "2"]}
        with self.assertRaises(ValueError) as err:
            plant.planting("Test", "4")
        self.assertEqual("The plantation is full!", str(err.exception))

    def test_planting_if_equal_to_size(self):
        plant = Plantation(3)
        plant.hire_worker("Test")
        plant.plants = {"Test1": ["1"], "Test2": ["1", "2"]}
        with self.assertRaises(ValueError) as err:
            plant.planting("Test", "4")
        self.assertEqual("The plantation is full!", str(err.exception))

    def test_str(self):
        plant = Plantation(4)
        plant.workers = ["Test1", "Test2"]
        plant.plants = {"Test1": ["1"], "Test2": ["2", "3"]}
        self.assertEqual(f"Plantation size: 4\n"
                         f"Test1, Test2\n"
                         f"Test1 planted: 1\n"
                         f"Test2 planted: 2, 3", str(plant))

    def test_repr_(self):
        plant = Plantation(4)
        plant.workers = ["Test1", "Test2"]
        plant.plants = {"Test1": ["1"], "Test2": ["2", "3"]}
        self.assertEqual(f'Size: 4\n'
                         f'Workers: Test1, Test2', repr(plant))





if __name__ == "__main__":
    main()
