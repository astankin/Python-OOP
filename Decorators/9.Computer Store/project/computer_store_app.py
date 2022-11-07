from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:

    def __init__(self):
        self.warehouse = []
        self.profits = 0
        self.valid_types = ["Desktop Computer", "Laptop"]

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer not in self.valid_types:
            raise ValueError(f"{ type_computer } is not a valid type computer!")
        if type_computer == "Desktop Computer":
            computer = DesktopComputer(manufacturer, model)
            computer.processor = processor
            computer.ram = ram
        elif type_computer == "Laptop":
            computer = Laptop(manufacturer, model)
            computer.processor = processor
            computer.ram = ram


    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int)

