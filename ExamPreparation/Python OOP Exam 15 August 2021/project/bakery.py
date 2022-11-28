from project.baked_food.bread import Bread
from project.baked_food.cake import Cake


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    def find_food(self, name):
        for food in self.food_menu:
            if food.name == name:
                return food

    @staticmethod
    def create_food(food_type: str, name: str, price: float):
        food = None
        if food_type == "Bread":
            food = Bread(name, price)
        elif food_type == "Cake":
            food = Cake(name, price)
        return food

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        if food_type not in ["Bread", "Cake"]:
            return
        if self.find_food(name):
            raise Exception(f"{food_type} {name} is already in the menu!")
        food = self.create_food(food_type, name, price)
        self.food_menu.append(food)
        return f"Added {food.name} ({type(food).__name__}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand:str):
        pass

    def add_table(self, table_type: str, table_number: int, capacity: int):
        pass

    def reserve_table(self, number_of_people: int):
        pass

    def order_food(self, table_number: int, *food_name):
        pass

    def order_drink(self, table_number: int, *drinks_name):
        pass

    def leave_table(self, table_number: int):
        pass

    def get_free_tables_info(self):
        pass

    def get_total_income(self):
        pass
