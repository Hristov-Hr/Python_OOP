from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:

    VALID_MUSICIANS = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):

        if musician_type not in self.VALID_MUSICIANS.keys():
            raise ValueError("Invalid musician type!")

        try:
            next(filter(lambda x: x.name == name, self.musicians))
            raise Exception(f"{name} is already a musician!")

        except StopIteration:
            self.musicians.append(self.VALID_MUSICIANS[musician_type](name, age))
            return f"{name} is now a {musician_type}."

    def create_band(self, name: str):

        try:
            next(filter(lambda x: x.name == name, self.bands))
            raise Exception(f"{name} band is already created!")

        except StopIteration:
            self.bands.append(Band(name))
            return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):

        try:
            concert = next(filter(lambda x: place == x.place, self.concerts))
            raise Exception(f"{place} is already registered for {concert.genre} concert!")

        except StopIteration:
            self.concerts.append(Concert(genre, audience, ticket_price, expenses, place))
            return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):

        musician = [m for m in self.musicians if m.name == musician_name]
        band = [b for b in self.bands if band_name == b.name]

        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")

        if not band:
            raise Exception(f"{band_name} isn't a band!")

        band[0].members.append(musician[0])
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):

        try:
            band = next(filter(lambda x: x.name == band_name, self.bands))
            try:
                musician = next(filter(lambda x: x.name == musician_name, band.members))
                band.members.remove(musician)
                return f"{musician.name} was removed from {band.name}."

            except StopIteration:
                raise Exception(f"{musician_name} isn't a member of {band.name}!")

        except StopIteration:
            raise Exception(f"{band_name} isn't a band!")

    def start_concert(self, concert_place: str, band_name: str):

        band = next(filter(lambda b: b.name == band_name, self.bands))
        band_members = [m.MUSICIAN_TYPE for m in band.members]
        needed_members = {"Singer", "Drummer", "Guitarist"}

        if not needed_members.issubset(band_members):
            raise Exception(f"{band.name} can't start the concert because it doesn't have enough members!")

        concert = next(filter(lambda c: c.place == concert_place, self.concerts))

        needed_skills = {"Rock": {"Drummer": "play the drums with drumsticks",
                                  "Singer": "sing high pitch notes",
                                  "Guitarist": "play rock"},
                         "Metal": {"Drummer": "play the drums with drumsticks",
                                   "Singer": "sing low pitch notes",
                                   "Guitarist": "play metal"},
                         "Jazz": {"Drummer": "play the drums with drum brushes",
                                  "Singer": "sing high pitch notes and sing low pitch notes",
                                  "Guitarist": "play jazz"}
                         }

        for member in band.members:
            if needed_skills[concert.genre][member.MUSICIAN_TYPE] not in member.skills:
                raise Exception(f"The {band.name} band is not ready to play at the concert!")

        profit = concert.audience * concert.ticket_price - concert.expenses

        return f"{band.name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}."
