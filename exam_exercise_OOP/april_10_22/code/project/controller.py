from typing import List

from project.player import Player
from project.supply.supply import Supply


class Controller:

    def __init__(self):
        self.players: List[Player] = []
        self.supplies: List[Supply] = []

    def add_player(self, *players: Player):

        names = []

        for player in players:
            if player not in self.players:
                names.append(player.name)
                self.players.append(player)

        return f"Successfully added: {', '.join(names)}"

    def add_supply(self, *supply: Supply):

        self.supplies.extend(supply)

    def sustain(self, player_name: str, sustenance_type: str):

        supplies = [s for s in self.supplies if s.SUPPLY_TYPE == sustenance_type]
        if not supplies:
            raise Exception(f"There are no {sustenance_type} supplies left!")
        supply = supplies.pop()

        players = [p for p in self.players if p.name == player_name]
        if players:
            player = players[0]
            if not player.need_sustenance:
                return f"{player.name} have enough stamina."

            self.supplies.remove(supply)
            new_stamina = player.stamina + supply.energy if player.stamina + supply.energy <= 100 else 100
            setattr(player, 'stamina', new_stamina)

            return f"{player.name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):

        first_player = [p for p in self.players if p.name == first_player_name][0]
        second_player = [p for p in self.players if p.name == second_player_name][0]

        zero_stamina = [f"Player {p.name} does not have enough stamina." for p in [first_player, second_player] if p.stamina == 0]
        if zero_stamina:
            return "\n".join(zero_stamina)

        duel_participants = sorted([first_player, second_player], key=lambda x: x.stamina)
        winner = self.battle(duel_participants[0], duel_participants[1])

        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            value = player.stamina - player.age * 2
            setattr(player, 'stamina', value if value > 0 else 0)
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = [p.__str__() for p in self.players]
        result.extend([s.details() for s in self.supplies])

        return "\n".join(result)

    @staticmethod
    def battle(first, second):
        setattr(second, 'stamina', second.stamina - first.stamina / 2)
        value = first.stamina - second.stamina / 2
        setattr(first, 'stamina', value if value > 0 else 0)

        return first if first.stamina > second.stamina else second
