import math
from abc import ABC, abstractmethod


class Computer(ABC):
    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if not value.strip():
            raise ValueError("Manufacturer name cannot be empty.")
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if not value.strip():
            raise ValueError("Model name cannot be empty.")
        self.__model = value

    @property
    @abstractmethod
    def processors(self):
        pass

    @property
    @abstractmethod
    def max_ram(self):
        pass

    @property
    def type_computer(self):
        return {"DesktopComputer": "desktop computer", "Laptop": "laptop"}

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.processors:
            raise ValueError(f"{processor} is not compatible with {self.type_computer[self.__class__.__name__]} {self.manufacturer} {self.model}!")
        if ram > self.max_ram or not self.__validate_ram(ram):
            raise ValueError(f"{ram}GB RAM is not compatible with {self.type_computer[self.__class__.__name__]} {self.manufacturer} {self.model}!")
        processor_price = self.processors[processor]
        ram_price = int(math.log2(ram)) * 100
        self.processor = processor
        self.ram = ram
        self.price = processor_price + ram_price
        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {self.price}$."

    @staticmethod
    def __validate_ram(ram):
        if ram == 0:
            return False
        while ram != 1:
            if ram % 2 != 0:
                return False
            ram = ram // 2
        return True

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"
