from project import FormulaTeam


class MercedesTeam(FormulaTeam):

    def calculate_revenue_after_race(self, race_pos: int):
        position_revenue = {
            1: 1100000, 2: 600000, 3: 600000, 4: 100000, 5: 100000, 6: 50000, 7: 50000
        }
        return self.add_result(position_revenue.get(race_pos, 0) - 200000)