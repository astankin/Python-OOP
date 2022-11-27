from abc import ABC, abstractmethod


class Astronaut(ABC):

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

    @abstractmethod
    def breathe(self):
        pass

    @abstractmethod
    def increase_oxygen(self, amount: int):
        pass

    def __str__(self):
        return f"Name: {self.name}\n" \
               f"Oxygen: {self.oxygen}\n" \
               f"Backpack items: {', '.join(self.backpack) if self.backpack else 'none'}"





