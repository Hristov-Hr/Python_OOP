from typing import List

from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    VALID_DIVER_TYPE = {"FreeDiver": FreeDiver, "ScubaDiver": ScubaDiver}
    VALID_FISH_TYPE = {"PredatoryFish": PredatoryFish, "DeepSeaFish": DeepSeaFish}

    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):

        if diver_type not in self.VALID_DIVER_TYPE.keys():
            return f"{diver_type} is not allowed in our competition."

        try:
            next(filter(lambda x: x.name == diver_name, self.divers))
            return f"{diver_name} is already a participant."

        except StopIteration:
            self.divers.append(self.VALID_DIVER_TYPE[diver_type](diver_name))
            return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):

        if fish_type not in self.VALID_FISH_TYPE.keys():
            return f"{fish_type} is forbidden for chasing in our competition."

        try:
            next(filter(lambda x: x.name == fish_name, self.fish_list))
            return f"{fish_name} is already permitted."

        except StopIteration:
            self.fish_list.append(self.VALID_FISH_TYPE[fish_type](fish_name, points))
            return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):

        try:
            diver = next(filter(lambda d: d.name == diver_name, self.divers))

        except StopIteration:
            return f"{diver_name} is not registered for the competition."

        try:
            fish = next(filter(lambda f: f.name == fish_name, self.fish_list))

        except StopIteration:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch or (diver.oxygen_level == fish.time_to_catch and not is_lucky):
            diver.miss(fish.time_to_catch)
            return f"{diver_name} missed a good {fish_name}."

        diver.hit(fish)
        return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):

        divers_for_recovery = [d for d in self.divers if d.has_health_issue]

        for diver in divers_for_recovery:
            diver.update_health_status()
            diver.renew_oxy()

        return f"Divers recovered: {len(divers_for_recovery)}"

    def diver_catch_report(self, diver_name: str):
        diver = [d for d in self.divers if d.name == diver_name][0]
        if diver:
            result = [f"**{diver_name} Catch Report**"]
            [result.append(f.fish_details()) for f in diver.catch]
            return "\n".join(result)

    def competition_statistics(self):

        result = ["**Nautical Catch Challenge Statistics**"]
        sorted_divers = sorted(self.divers, key=lambda x: (-x.competition_points, -len(x.catch), x.name))
        [result.append(str(d)) for d in sorted_divers if not d.has_health_issue]

        return "\n".join(result)


