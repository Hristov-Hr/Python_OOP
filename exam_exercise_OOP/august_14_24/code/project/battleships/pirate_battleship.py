from project.battleships.base_battleship import BaseBattleship


class PirateBattleship(BaseBattleship):

    def __init__(self, name: str, health: int, hit_strength: int):
        super().__init__(name, health, hit_strength, ammunition=80)

    def attack(self):
        self.ammunition = max(self.ammunition - 10, 0)
