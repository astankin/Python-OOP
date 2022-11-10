class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


car = Car("a", "b", 1, 4)
car.make = ""
print(car)

from unittest import TestCase, main


class CatTest(TestCase):

    def test_initialization_with_correct_value(self):
        test_car = Car("Opel", "Corsa", 7, 50)
        self.assertEqual("Opel", test_car.make)
        self.assertEqual("Corsa", test_car.model)
        self.assertEqual(7, test_car.fuel_consumption)
        self.assertEqual(50, test_car.fuel_capacity)
        self.assertEqual(0, test_car.fuel_amount)

    def test_initialization_with_incorrect_car_make_raises(self):
        with self.assertRaises(Exception) as ex:
            test_car = Car("", "Corsa", 7, 50)
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_initialization_with_incorrect_car_model_raises(self):
        with self.assertRaises(Exception) as ex:
            test_car = Car("Opel", "", 7, 50)
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_with_zero_value_raises(self):
        with self.assertRaises(Exception) as ex:
            test_car = Car("Opel", "Corsa", 0, 50)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_consumption_with_negative_value_raises(self):
        with self.assertRaises(Exception) as ex:
            test_car = Car("Opel", "Corsa", -15, 50)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_with_zero_value_raises(self):
        with self.assertRaises(Exception) as ex:
            test_car = Car("Opel", "Corsa", 5, 0)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_with_negative_value_raises(self):
        with self.assertRaises(Exception) as ex:
            test_car = Car("Opel", "Corsa", 5, -50)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_with_negative_value_raises(self):
        with self.assertRaises(Exception) as ex:
            test_car = Car("Opel", "Corsa", 5, 50)
            test_car.fuel_amount = -5
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_with_amount_lower_then_fuel_capacity(self):
        test_car = Car("Opel", "Corsa", 5, 50)
        test_car.refuel(7)
        self.assertEqual(7, test_car.fuel_amount)

    def test_refuel_with_amount_higher_then_fuel_capacity(self):
        test_car = Car("Opel", "Corsa", 5, 50)
        test_car.refuel(70)
        self.assertEqual(50, test_car.fuel_amount)

    def test_refuel_with_negative_amount_raises(self):
        test_car = Car("Opel", "Corsa", 5, 50)
        with self.assertRaises(Exception) as ex:
            test_car.refuel(-70)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_with_zero_amount_raises(self):
        test_car = Car("Opel", "Corsa", 5, 50)
        with self.assertRaises(Exception) as ex:
            test_car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_drive_with_distance_amount_and_enough_fuel(self):
        test_car = Car("Opel", "Corsa", 5, 50)
        test_car.refuel(20)
        test_car.drive(100)
        self.assertEqual(15, test_car.fuel_amount)

    def test_drive_with_distance_bigger_then_fuel_raises(self):
        test_car = Car("Opel", "Corsa", 5, 50)
        test_car.refuel(4)
        with self.assertRaises(Exception) as ex:
            test_car.drive(100)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == "__main__":
    main()
