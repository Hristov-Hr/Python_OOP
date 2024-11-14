from typing import List

from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:

    EQUIPMENT_TYPES = {"KneePad": KneePad, "ElbowPad": ElbowPad}
    TEAMS_TYPES = {"OutdoorTeam": OutdoorTeam, "IndoorTeam": IndoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):

        if equipment_type not in self.EQUIPMENT_TYPES.keys():
            raise Exception("Invalid equipment type!")

        self.equipment.append(self.EQUIPMENT_TYPES[equipment_type]())
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):

        if team_type not in self.TEAMS_TYPES.keys():
            raise Exception("Invalid team type!")

        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."

        self.teams.append(self.TEAMS_TYPES[team_type](team_name, country, advantage))
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):

        team = [t for t in self.teams if t.name == team_name][0]
        equip = [e for e in self.equipment if equipment_type == e.__class__.__name__][-1]

        if equip.price > team.budget:
            raise Exception("Budget is not enough!")

        team.budget -= equip.price
        team.equipment.append(equip)
        self.equipment.remove(equip)

        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):

        try:
            team = next(filter(lambda t: t.name == team_name, self.teams))

        except StopIteration:
            raise Exception("No such team!")

        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):

        counter = 0

        for e in self.equipment:
            if equipment_type == e.__class__.__name__:
                e.increase_price()
                counter += 1

        return f"Successfully changed {counter}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):

        first_team = [t for t in self.teams if t.name == team_name1][0]
        second_team = [t for t in self.teams if t.name == team_name2][0]

        if first_team.__class__.__name__ != second_team.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        first_team_result = first_team.advantage + sum(p.protection for p in first_team.equipment)
        second_team_result = second_team.advantage + sum(p.protection for p in second_team.equipment)

        if first_team_result == second_team_result:
            return "No winner in this game."

        winner = first_team if first_team_result > second_team_result else second_team
        winner.win()

        return f"The winner is {winner.name}."

    def get_statistics(self):

        result = [f"Tournament: {self.name}", f"Number of Teams: {len(self.teams)}", "Teams:"]

        [result.append(t.get_statistics()) for t in sorted(self.teams, key=lambda x: -x.wins)]

        return "\n".join(result)