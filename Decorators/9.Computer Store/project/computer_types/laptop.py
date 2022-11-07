import math

from project.computer_types.computer import Computer


class Laptop(Computer):
    ALLOWED_PROCESSORS = {
        "AMD Ryzen 9 5950X": 900,
        "Intel Core i9-11900H": 1050,
        "Apple M1 Pro": 1200
    }
    MAX_RAM = 64

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.ALLOWED_PROCESSORS:
            raise ValueError(f"{processor} is not compatible with laptop {self.manufacturer} {self.model}!")
        if not self.ram_is_valid(ram):
            raise ValueError(f"{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!")
        self.processor = processor
        self.ram = ram
        computer_price = self.ALLOWED_PROCESSORS[processor] + self.ram_price(ram)
        return f"Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {computer_price}$."

    @staticmethod
    def ram_is_valid(ram):
        if ram <= Laptop.MAX_RAM:
            if ram == 0:
                return False
            while ram != 1:
                if ram % 2 != 0:
                    return False
                ram = ram // 2
            return True

    @staticmethod
    def ram_price(ram):
        return int(math.log2(ram) * 100)


