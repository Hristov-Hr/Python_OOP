from project.peaks.base_peak import BasePeak


class SummitPeak(BasePeak):

    def get_recommended_gear(self):
        gears = ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]
        #ToDo

    def calculate_difficulty_level(self):
        if self.elevation > 2500:
            return "Extreme"
        if self.elevation >= 1500:
            return "Advanced"