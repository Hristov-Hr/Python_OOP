from project import MercedesTeam
from project import RedBullTeam


class F1SeasonApp:

    def __init__(self):
        self.red_bull_team: RedBullTeam is None
        self.mercedes_team: MercedesTeam is None

    @classmethod
    def register_team_for_season(cls, team_name: str, budget: int):
        if team_name not in ["Red Bull", "Mercedes"]:
            raise ValueError("Invalid team name!")
        if team_name == "Red Bull":
            cls.red_bull_team = RedBullTeam(budget)

        elif team_name == "Mercedes":
            cls.mercedes_team = MercedesTeam(budget)
        return f"{team_name} has joined the new F1 season."

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        try:
            winner = "Red Bull" if red_bull_pos < mercedes_pos else "Mercedes"

            return f"Red Bull: {self.red_bull_team.calculate_revenue_after_race(red_bull_pos)}. Mercedes: {self.mercedes_team.calculate_revenue_after_race(mercedes_pos)}. {winner} is ahead at the {race_name} race."

        except AttributeError:
            raise Exception("Not all teams have registered for the season.")

