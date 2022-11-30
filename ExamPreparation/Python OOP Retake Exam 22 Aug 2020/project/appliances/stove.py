from project.appliances.appliance import Appliance


class Stove(Appliance):
    def __init__(self):
        super().__init__(0.7)

    def get_monthly_expense(self):
        return self.cost * 30
