from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    EXPENSES = 200000

    def __init__(self, budget: int):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = self.__get_amount(race_pos) - self.EXPENSES
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"

    @staticmethod
    def __get_amount(rase_pos):
        sponsors_amount = {
            1: 1000000,
            3: 500000,
            5: 100000,
            7: 500000
        }
        return sponsors_amount[rase_pos]
