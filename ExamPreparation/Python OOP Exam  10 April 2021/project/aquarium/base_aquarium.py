from abc import ABC, abstractmethod


class BaseAquarium(ABC):

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum([decoration.comfort for decoration in self.decorations])

    @property
    @abstractmethod
    def fish_type(self):
        pass

    def add_fish(self, fish):
        if self.capacity == len(self.fish):
            return "Not enough capacity."
        if self.fish_type != fish.__class__.__name__:
            return 'Water not suitable.'
        self.fish.append(fish)
        return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        result = [f"{self.name}:"]
        if not self.fish:
            result.append("Fish: none")
        else:
            result.append(f"Fish: {' '.join([fish.name for fish in self.fish])}")
        result.append(f"Decorations: {len(self.decorations)}")
        result.append(f"Comfort: {self.calculate_comfort()}")
        return '\n'.join(result)

