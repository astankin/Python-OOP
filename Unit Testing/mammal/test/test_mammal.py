from unittest import TestCase, main

from project.mammal import Mammal


class MammalTest(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("name", "type", "sound")

    def test_initialization(self):
        self.assertEqual("name", self.mammal.name)
        self.assertEqual("type", self.mammal.type)
        self.assertEqual("sound", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        result = self.mammal.make_sound()
        self.assertEqual("name makes sound", result)

    def test_get_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info(self):
        result = self.mammal.info()
        self.assertEqual("name is of type type", result)


if __name__ == "__main__":
    main()