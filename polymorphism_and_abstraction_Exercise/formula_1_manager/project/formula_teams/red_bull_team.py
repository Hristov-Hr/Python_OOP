from project import FormulaTeam


class RedBullTeam(FormulaTeam):

    def calculate_revenue_after_race(self, race_pos: int):
        position_revenue = {
            1: 1520000, 2: 820000, 3: 20000, 4: 20000, 5: 20000, 6: 20000,
            7: 20000, 8: 20000, 9: 10000, 10: 10000
        }
        return self.add_result(position_revenue.get(race_pos, 0) - 250000)






