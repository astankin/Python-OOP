from unittest import TestCase, main

from project.pet_shop import PetShop


class TestPetShop(TestCase):
    def test_init(self):
        shop = PetShop("Test")
        self.assertEqual("Test", shop.name)
        self.assertEqual({}, shop.food)
        self.assertEqual([], shop.pets)

    def test_add_food_raise(self):
        shop = PetShop("Test")
        with self.assertRaises(ValueError) as err:
            shop.add_food("food", 0)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(err.exception))
        with self.assertRaises(ValueError) as err:
            shop.add_food("food", -5)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(err.exception))

    def test_add_food(self):
        shop = PetShop("Test")
        result = shop.add_food("food", 10)
        self.assertEqual(f"Successfully added 10.00 grams of food.", result)
        self.assertEqual({"food": 10}, shop.food)
        result = shop.add_food("food", 10)
        self.assertEqual(f"Successfully added 10.00 grams of food.", result)
        self.assertEqual({"food": 20}, shop.food)

    def test_add_pet_if_pet_name_not_in_collection(self):
        shop = PetShop("Test")
        result = shop.add_pet("dog")
        self.assertEqual(f"Successfully added dog.", result)
        self.assertEqual(["dog"], shop.pets)

    def test_add_pet_raise(self):
        shop = PetShop("Test")
        shop.add_pet("dog")
        with self.assertRaises(Exception) as ex:
            shop.add_pet("dog")
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))
        self.assertEqual(["dog"], shop.pets)

    def test_feed_pet_raise(self):
        shop = PetShop("Test")
        shop.add_food("food", 10)
        with self.assertRaises(Exception) as ex:
            shop.feed_pet("food", "dog")
        self.assertEqual(f"Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_food_not_in_collection(self):
        shop = PetShop("Test")
        shop.add_pet("dog")
        shop.add_food("food", 10)
        result = shop.feed_pet("food1", "dog")
        self.assertEqual(f'You do not have food1', result)

    def test_feed_pet_food_not_enough(self):
        shop = PetShop("Test")
        shop.add_pet("dog")
        shop.add_food("food", 10)
        result = shop.feed_pet("food", "dog")
        self.assertEqual("Adding food...", result)
        self.assertEqual({"food": 1010}, shop.food)

    def test_feed_pet_food_correct_values(self):
        shop = PetShop("Test")
        shop.add_pet("dog")
        shop.add_food("food", 1000)
        result = shop.feed_pet("food", "dog")
        self.assertEqual(f"dog was successfully fed", result)
        self.assertEqual({"food": 900}, shop.food)

    def test_repr(self):
        shop = PetShop("Test")
        shop.add_pet("dog1")
        shop.add_pet("dog2")
        shop.add_pet("dog3")
        expected = f'Shop Test:\n' \
                   f'Pets: dog1, dog2, dog3'
        self.assertEqual(expected, repr(shop))

if __name__ == "__main__":
    main()
