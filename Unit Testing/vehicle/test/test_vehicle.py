from unittest import TestCase, main

from project.vehicle import Vehicle


class VehicleTest(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(125, 200)

    def test_initialisation(self):
        self.assertEqual(125, self.vehicle.fuel)
        self.assertEqual(200, self.vehicle.horse_power)
        self.assertEqual(125, self.vehicle.capacity)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_if_the_fuel_is_enough(self):
        self.vehicle.drive(100)
        self.assertEqual(0, self.vehicle.fuel)

    def test_drive_if_fuel_is_not_enough_raises(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(150)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_if_fuel_is_not_too_much(self):
        self.vehicle.drive(100)
        self.vehicle.refuel(80)
        self.assertEqual(80, self.vehicle.fuel)

    def test_if_fuel_amount_is_too_much(self):
        self.vehicle.drive(100)
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(150)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str(self):
        expected = f"The vehicle has 200 horse power with 125 fuel left and 1.25 fuel consumption"
        actual = str(self.vehicle)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()