from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    EXPENSES = 250000

    def __init__(self, budget: int):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = self.__get_amount(race_pos) - self.EXPENSES
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"

    @staticmethod
    def __get_amount(rase_pos):
        sponsors_amount = {
            1: 1500000,
            2: 800000,
            8: 20000,
            10: 10000
        }
        return sponsors_amount[rase_pos]

