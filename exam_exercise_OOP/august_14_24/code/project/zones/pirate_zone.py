from project.battleships.royal_battleship import RoyalBattleship
from project.zones.base_zone import BaseZone


class PirateZone(BaseZone):

    def __init__(self, code):
        super().__init__(code, volume=8)

    def zone_info(self):
        info = ["@Pirate Zone Statistics@", f"Code: {self.code}; Volume: {self.volume}",
                f"Battleships currently in the Pirate Zone: {len(self.ships)}, "
                f"{len([s for s in self.ships if isinstance(s, RoyalBattleship)])} out of them are Royal Battleships."]

        if self.ships:
            info.append(f"#{', '.join(s.name for s in self.get_ships())}#")

        return "\n".join(info)