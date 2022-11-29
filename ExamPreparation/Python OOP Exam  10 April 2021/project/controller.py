from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def __find_aquarium(self, name):
        for aquarium in self.aquariums:
            if aquarium.name == name:
                return aquarium
        return None

    @staticmethod
    def __create_aquarium(aquarium_type, aquarium_name):
        if aquarium_type == "FreshwaterAquarium":
            return FreshwaterAquarium(aquarium_name)
        elif aquarium_type == "SaltwaterAquarium":
            return SaltwaterAquarium(aquarium_name)

    @staticmethod
    def __create_decoration(decoration_type):
        if decoration_type == "Ornament":
            return Ornament()
        elif decoration_type == "Plant":
            return Plant()

    @staticmethod
    def __create_fish(fish_type, fish_name, species, price):
        if fish_type == "FreshwaterFish":
            return FreshwaterFish(fish_name, species, price)
        elif fish_type == "SaltwaterFish":
            return SaltwaterFish(fish_name, species, price)

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in ["FreshwaterAquarium", "SaltwaterAquarium"]:
            return "Invalid aquarium type."
        aquarium = self.__create_aquarium(aquarium_type, aquarium_name)
        self.aquariums.append(aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in ["Ornament", "Plant"]:
            return f"Invalid decoration type."
        decoration = self.__create_decoration(decoration_type)
        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium = self.__find_aquarium(aquarium_name)
        decoration = self.decorations_repository.find_by_type(decoration_type)
        if not decoration:
            return f"There isn't a decoration of type {decoration_type}."
        if aquarium is None:
            return
        aquarium.add_decoration(decoration)
        self.decorations_repository.remove(decoration)
        return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type not in ["FreshwaterFish", "SaltwaterFish"]:
            return f"There isn't a fish of type {fish_type}."
        fish = self.__create_fish(fish_type, fish_name, fish_species, price)
        aquarium = self.__find_aquarium(aquarium_name)
        if fish_type == "FreshwaterFish" and type(aquarium).__name__ == "FreshwaterAquarium":
            return aquarium.add_fish(fish)
        elif fish_type == "SaltwaterFish" and type(aquarium).__name__ == "SaltwaterAquarium":
            return aquarium.add_fish(fish)
        return "Water not suitable."

    def feed_fish(self, aquarium_name: str):
        aquarium = self.__find_aquarium(aquarium_name)
        aquarium.feed()
        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self.__find_aquarium(aquarium_name)
        decoration_value = sum([decoration.price for decoration in aquarium.decorations])
        fish_value = sum([fish.price for fish in aquarium.fish])
        value = fish_value + decoration_value
        return f"The value of Aquarium {aquarium_name} is {value:.2f}."

    def report(self):
        result = []
        for aquarium in self.aquariums:
            result.append(str(aquarium))
        return '\n'.join(result)
