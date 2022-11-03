from project.formula_teams.mercedes_team import MercedesTeam
from project.formula_teams.red_bull_team import RedBullTeam


class F1SeasonApp:
    red_bull_team = None
    mercedes_team = None

    def __init__(self):
        pass

    def register_team_for_season(self, team_name: str, budget: int):
        if team_name not in ["Red Bull", "Mercedes"]:
            raise ValueError("Invalid team name!")
        if team_name == "Red Bull":
            F1SeasonApp.red_bull_team = RedBullTeam(budget)
        elif team_name == "Mercedes":
            F1SeasonApp.mercedes_team = MercedesTeam(budget)
        return f"{team_name} has joined the new F1 season."

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        if F1SeasonApp.red_bull_team is None or F1SeasonApp.mercedes_team is None:
            raise Exception("Not all teams have registered for the season.")
        return f"Red Bull: {F1SeasonApp.red_bull_team.calculate_revenue_after_race(red_bull_pos)}. " \
               f"Mercedes: {F1SeasonApp.mercedes_team.calculate_revenue_after_race(mercedes_pos)}. " \
               f"{self.__get_better_team(red_bull_pos, mercedes_pos)} is ahead at the {race_name} race."

    @staticmethod
    def __get_better_team(red_bull_pos, mercedes_pos):
        if red_bull_pos < mercedes_pos:
            return "Red Bull"
        elif mercedes_pos < red_bull_pos:
            return "Mercedes"
