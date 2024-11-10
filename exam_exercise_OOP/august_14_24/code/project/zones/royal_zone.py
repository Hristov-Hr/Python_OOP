from project.battleships.pirate_battleship import PirateBattleship
from project.zones.base_zone import BaseZone


class RoyalZone(BaseZone):

    def __init__(self, code: str):
        super().__init__(code, volume=10)

    def zone_info(self):
        info = ["@Royal Zone Statistics@", f"Code: {self.code}; Volume: {self.volume}",
                f"Battleships currently in the Royal Zone: {len(self.ships)}, "
                f"{len([s for s in self.ships if isinstance(s, PirateBattleship)])} out of them are Pirate Battleships."]

        if self.ships:
            info.append(f"#{', '.join(s.name for s in self.get_ships())}#")

        return "\n".join(info)