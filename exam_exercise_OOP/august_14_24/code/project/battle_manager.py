from project.battleships.base_battleship import BaseBattleship
from project.battleships.pirate_battleship import PirateBattleship
from project.battleships.royal_battleship import RoyalBattleship
from project.zones.base_zone import BaseZone
from project.zones.pirate_zone import PirateZone
from project.zones.royal_zone import RoyalZone


class BattleManager:

    VALID_TYPES_ZONES = {"RoyalZone": RoyalZone, "PirateZone": PirateZone}
    VALID_SHIP_TYPES = {'RoyalBattleship': RoyalBattleship, 'PirateBattleship': PirateBattleship}

    def __init__(self):

        self.zones = []
        self.ships = []

    def add_zone(self, zone_type: str, zone_code: str):

        if zone_type not in self.VALID_TYPES_ZONES.keys():
            raise Exception("Invalid zone type!")

        try:
            next(filter(lambda z: z.code == zone_code, self.zones))
            return "Zone already exists!"
        except StopIteration:
            self.zones.append(self.VALID_TYPES_ZONES[zone_type](zone_code))
            return f"A zone of type {zone_type} was successfully added."

    def add_battleship(self, ship_type: str, name: str, health: int, hit_strength: int):

        if ship_type not in self.VALID_SHIP_TYPES.keys():
            raise Exception(f"{ship_type} is an invalid type of ship!")

        self.ships.append(self.VALID_SHIP_TYPES[ship_type](name, health, hit_strength))
        return f"A new {ship_type} was successfully added."

    @staticmethod
    def add_ship_to_zone(zone: BaseZone, ship: BaseBattleship):

        if zone.volume <= 0:
            return f"Zone {zone.code} does not allow more participants!"

        if ship.health <= 0:
            return f"Ship {ship.name} is considered sunk! Participation not allowed!"

        if not ship.is_available:
            return f"Ship {ship.name} is not available and could not participate!"

        zone_type = "royal" if isinstance(zone, RoyalZone) else "pirate"
        ship_type = "pirate" if isinstance(ship, PirateBattleship) else "royal"

        ship.is_attacking = False if zone_type != ship_type else True
        ship.is_available = False
        zone.ships.append(ship)
        zone.volume -= 1

        return f"Ship {ship.name} successfully participated in zone {zone.code}."

    def remove_battleship(self, ship_name: str):

        try:
            ship = next(filter(lambda s: s.name == ship_name, self.ships))

        except StopIteration:
            return f"No ship with this name!"

        if not ship.is_available:
            return "The ship participates in zone battles! Removal is impossible!"

        self.ships.remove(ship)

        return f"Successfully removed ship {ship_name}."

    def start_battle(self, zone: BaseZone):

        attackers = [s for s in zone.ships if s.is_attacking]
        targets = [s for s in zone.ships if not s.is_attacking]

        if not attackers or not targets:
            return "Not enough participants. The battle is canceled."

        most_powerful_ship = sorted(attackers, key=lambda x: -x.hit_strength)[0]
        most_healthiest_ship = sorted(targets, key=lambda x: -x.health)[0]

        most_powerful_ship.attack()
        most_healthiest_ship.take_damage(most_powerful_ship)

        if most_healthiest_ship.health <= 0:
            zone.ships.remove(most_healthiest_ship)
            self.ships.remove(most_healthiest_ship)

            return f"{most_healthiest_ship.name} lost the battle and was sunk."

        if most_powerful_ship.ammunition <= 0:
            zone.ships.remove(most_powerful_ship)
            self.ships.remove(most_powerful_ship)

            return f"{most_powerful_ship.name} ran out of ammunition and leaves."

        return "Both ships survived the battle."

    def get_statistics(self):

        result = []

        available_ships = [s for s in self.ships if s.is_available]
        if available_ships:
            result.append(f"Available Battleships: {len(available_ships)}")
            result.append(f"#{', '.join(a.name for a in available_ships)}#")

        if self.zones:
            result.append("***Zones Statistics:***")
            result.append(f"Total Zones: {len(self.zones)}")
            for z in sorted(self.zones, key=lambda x: x.code):
                result.append(z.zone_info())

        return "\n".join(result)



