from project.formula_teams.red_bull_team import RedBullTeam


class F1SeasonApp:
    red_bull_team = None
    mercedes_team = None

    def __init__(self):
        pass

    def register_team_for_season(self, team_name: str, budget: int):
        if team_name not in ["Red Bull", "Mercedes"]:
            raise ValueError("Invalid team name!")
        red_bull_team = RedBullTeam(budget)
        return f"{team_name} has joined the new F1 season."
