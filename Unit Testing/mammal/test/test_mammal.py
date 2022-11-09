from unittest import TestCase, main

from project.mammal import Mammal


class MammalTest(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("name", "type", "sound")

    def test_initialization(self):
        self.assertEqual("name", self.mammal.name)
        self.assertEqual("type", self.mammal.type)
        self.assertEqual("sound", self.mammal.sound)

    def test_make_sound(self):
        self.assertEqual("name makes sound", f"{self.mammal.name} makes {self.mammal.sound}")

    def test_get_kingdom(self):
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_info(self):
        self.assertEqual("name is of type type", f"{self.mammal.name} is of type {self.mammal.type}")


if __name__ == "__main__":
    main()