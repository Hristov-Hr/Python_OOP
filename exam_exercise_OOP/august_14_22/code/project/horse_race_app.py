from typing import List

from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:

    HORSE_TYPES = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}

    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    def add_horse(self, horse_type, horse_name, horse_speed):
        try:
            next(filter(lambda x: horse_name == x.name, self.horses))
            raise Exception(f"Horse {horse_name} has been already added!")

        except StopIteration:
            if horse_type in self.HORSE_TYPES.keys():
                self.horses.append(self.HORSE_TYPES[horse_type](horse_name, horse_speed))
                return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name, age):
        try:
            next(filter(lambda x: jockey_name == x.name, self.jockeys))
            raise Exception(f"Jockey {jockey_name} has been already added!")

        except StopIteration:
            self.jockeys.append(Jockey(jockey_name, age))
            return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type):
        try:
            next(filter(lambda x: race_type == x.race_type, self.horse_races))
            raise Exception(f"Race {race_type} has been already created!")

        except StopIteration:
            self.horse_races.append(HorseRace(race_type))
            return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name, horse_type):
        try:
            jockey = next(filter(lambda x: x.name == jockey_name, self.jockeys))

            for horse in self.horses:
                if not horse.is_taken:
                    if jockey.horse is None:
                        jockey.horse = horse
                        horse.is_taken = True
                        return f"Jockey {jockey_name} will ride the horse {horse.name}."

                    else:
                        return f"Jockey {jockey_name} already has a horse."

            else:
                raise Exception(f"Horse breed {horse_type} could not be found!")

        except StopIteration:
            raise Exception(f"Jockey {jockey_name} could not be found!")

    def add_jockey_to_horse_race(self, race_type, jockey_name):
        try:
            race = next(filter(lambda x: race_type == x.race_type, self.horse_races))

        except StopIteration:
            raise Exception(f"Race {race_type} could not be found!")

        try:
            jockey = next(filter(lambda x: x.name == jockey_name, self.jockeys))
            if not jockey.horse:
                raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        except StopIteration:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        try:
            next(filter(lambda x: x.name == jockey.name, race.jockeys))
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        except StopIteration:
            race.jockeys.append(jockey)
            return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type):
        try:
            race = next(filter(lambda x: race_type == x.race_type, self.horse_races))
            if len(race.jockeys) < 2:
                raise Exception(f"Horse race {race_type} needs at least two participants!")

        except StopIteration:
            raise Exception(f"Race {race_type} could not be found!")

        winner = [j for j in race.jockeys if j.horse.speed == max(j.horse.speed for j in race.jockeys)][0]

        return f"The winner of the {race_type} race, with a speed of {winner.horse.speed}km/h is {winner.name}! " \
               f"Winner's horse: {winner.horse.name}."