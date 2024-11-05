from typing import List

from project.climbers.arctic_climber import ArcticClimber
from project.climbers.base_climber import BaseClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.base_peak import BasePeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:

    VALID_CLIMBERS_TYPE = {"ArcticClimber": ArcticClimber, "SummitClimber": SummitClimber}
    VALID_PEAKS_TYPE = {"ArcticPeak": ArcticPeak, "SummitPeak": SummitPeak}

    def __init__(self):
        self.climbers: List[BaseClimber] = []
        self.peaks: List[BasePeak] = []

    def register_climber(self, climber_type: str, climber_name: str):

        if climber_type not in self.VALID_CLIMBERS_TYPE.keys():
            return f"{climber_type} doesn't exist in our register."

        try:
            next(filter(lambda c: c.name == climber_name, self.climbers))
            return f"{climber_name} has been already registered."

        except StopIteration:
            climber = self.VALID_CLIMBERS_TYPE[climber_type](climber_name)
            self.climbers.append(climber)
            return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in self.VALID_PEAKS_TYPE.keys():
            return f"{peak_type} is an unknown type of peak."

        try:
            next(filter(lambda p: p.name == peak_name, self.peaks))
        except StopIteration:
            peak = self.VALID_PEAKS_TYPE[peak_type](peak_name, peak_elevation)
            self.peaks.append(peak)
            return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]):

        climber = next(filter(lambda c: c.name == climber_name, self.climbers))
        peak = next(filter(lambda p: p.name == peak_name, self.peaks))

        if gear == peak.get_recommended_gear():
            return f"{climber_name} is prepared to climb {peak_name}."

        climber.is_prepared = False
        return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(sorted(g for g in peak.get_recommended_gear() if g not in gear))}."

    def perform_climbing(self, climber_name: str, peak_name: str):

        try:
            climber = next(filter(lambda c: c.name == climber_name, self.climbers))
        except StopIteration:
            return f"Climber {climber_name} is not registered yet."

        try:
            peak = next(filter(lambda p: p.name == peak_name, self.peaks))
        except StopIteration:
            return f"Peak {peak_name} is not part of the wish list."

        if climber.is_prepared and climber.can_climb():
            climber.climb(peak)
            return f"{climber.name} conquered {peak.name} whose difficulty level is {peak.difficulty_level}."

        if not climber.is_prepared:
            return f"{climber.name} will need to be better prepared next time."

        climber.rest()
        return f"{climber.name} needs more strength to climb {peak.name} and is therefore taking some rest."

    def get_statistics(self):
        sorted_climbers = sorted([climber for climber in self.climbers if climber.conquered_peaks],
                                 key=lambda climber: (-len(climber.conquered_peaks), climber.name))

        result = [
            f"Total climbed peaks: {len(self.peaks)}",
            "**Climber's statistics:**"
        ]

        climber_statistics = "\n".join(str(c) for c in sorted_climbers)
        result.append(climber_statistics)

        return '\n'.join(result)
        # climbers_with_conquered_peak = [c for c in self.climbers if len(c.conquered_peaks) > 0]
        # sorted_climbers = sorted(climbers_with_conquered_peak, key=lambda x: (-len(x.conquered_peaks), x.name))
        # conquered_peaks = len({p for c in sorted_climbers for p in c.conquered_peaks})
        #
        # result = [f"Total climbed peaks: {conquered_peaks}", "**Climber's statistics:**"]
        # result.append(str(c) for c in sorted_climbers)
        #
        # return result
