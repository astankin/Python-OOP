from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if self.__find_delicacy_by_name(name):
            raise Exception(f"{name} already exists!")

        if type_delicacy not in ["Gingerbread", "Stolen"]:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        delicacy = self.__create_delicacy(type_delicacy, name, price)
        self.delicacies.append(delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if self.__find_booth_by_number(booth_number):
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in ["Open Booth", "Private Booth"]:
            raise Exception(f"{type_booth} is not a valid booth!")

        booth = self.__create_booth(type_booth, booth_number, capacity)
        self.booths.append(booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):

        booth = self.__get_suitable_booth(number_of_people)
        if booth is None:
            raise Exception(f"No available booth for {number_of_people} people!")
        booth.reserve(number_of_people)
        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = self.__find_booth_by_number(booth_number)
        if booth is None:
            raise Exception(f"Could not find booth {booth_number}!")

        delicacy = self.__find_delicacy_by_name(delicacy_name)
        if delicacy is None:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = self.__find_booth_by_number(booth_number)
        delicacy_amount = 0
        for delicacy in booth.delicacy_orders:
            delicacy_amount += delicacy.price
        booth_bill = delicacy_amount + booth.price_for_reservation
        self.income += booth_bill
        booth.delicacy_orders = []
        booth.price_for_reservation = 0
        booth.is_reserved = False
        return f"Booth {booth_number}:\n" \
               f"Bill: {booth_bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

    def __get_suitable_booth(self, number_of_people):
        for booth in self.booths:
            if booth.capacity >= number_of_people and not booth.is_reserved:
                return booth
        return None

    def __find_booth_by_number(self, booth_number):
        for booth in self.booths:
            if booth.booth_number == booth_number:
                return booth
        return None

    def __create_booth(self, type_booth, booth_number, capacity):
        if type_booth == "Open Booth":
            return OpenBooth(booth_number, capacity)
        if type_booth == "Private Booth":
            return PrivateBooth(booth_number, capacity)



    def __find_delicacy_by_name(self, delicacy_name):
        for delicacy in self.delicacies:
            if delicacy.name == delicacy_name:
                return delicacy
        return None


    def __create_delicacy(self, delicacy_type, name, price):
        if delicacy_type == "Gingerbread":
            return Gingerbread(name, price)
        if delicacy_type == "Stolen":
            return Stolen(name, price)

