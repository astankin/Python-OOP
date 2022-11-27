from abc import ABC, abstractmethod


class Astronaut(ABC):
    decrease_coefficient = 10

    @abstractmethod
    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    def breathe(self):
        self.oxygen -= self.decrease_coefficient

    def increase_oxygen(self, amount: int):
        self.oxygen += amount

    def __str__(self):
        return f"Name: {self.name}\n" \
               f"Oxygen: {self.oxygen}\n" \
               f"Backpack items: {', '.join(self.backpack) if self.backpack else 'none'}"





