from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):

    def __init__(self, name):
        super().__init__(name, strength=150)

    def can_climb(self):
        return self.strength >= 75

    def climb(self, peak: BasePeak):
        if peak.difficulty_level == "Advanced":
            self.strength -= 39
        else:
            self.strength -= 75

        self.conquered_peaks.append(peak.name)
