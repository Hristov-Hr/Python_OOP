from typing import List

from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:

    DELICACIES_TYPE = {"Gingerbread": Gingerbread, "Stolen": Stolen}
    BOOTHS_TYPE = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        try:
            next(filter(lambda x: x.name == name, self.delicacies))
            raise Exception(f"{name} already exists!")

        except StopIteration:
            if type_delicacy not in self.DELICACIES_TYPE.keys():
                raise Exception(f"{type_delicacy} is not on our delicacy menu!")

            delicacy = self.DELICACIES_TYPE[type_delicacy](name, price)
            self.delicacies.append(delicacy)
            return f"Added delicacy {delicacy.name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        try:
            next(filter(lambda x: booth_number == x.booth_number, self.booths))
            raise Exception(f"Booth number {booth_number} already exists!")

        except StopIteration:
            if type_booth not in self.BOOTHS_TYPE.keys():
                raise Exception(f"{type_booth} is not a valid booth!")

            booth = self.BOOTHS_TYPE[type_booth](booth_number, capacity)
            self.booths.append(booth)
            return f"Added booth number {booth.booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):

        for booth in self.booths:
            if booth.capacity >= number_of_people and not booth.is_reserved:
                booth.reserve(number_of_people)
                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        try:
            booth = next(filter(lambda x: x.booth_number == booth_number, self.booths))
            try:
                delicacy = next(filter(lambda x: x.name == delicacy_name, self.delicacies))
                booth.delicacy_orders.append(delicacy)
                return f"Booth {booth.booth_number} ordered {delicacy.name}."

            except StopIteration:
                raise Exception(f"No {delicacy_name} in the pastry shop!")

        except StopIteration:
            raise Exception(f"Could not find booth {booth_number}!")

    def leave_booth(self, booth_number: int):
        booth = next(filter(lambda x: x.booth_number == booth_number, self.booths))
        bill = booth.price_for_reservation + sum(d.price for d in booth.delicacy_orders)
        self.income += bill
        booth.price_for_reservation = 0
        booth.is_reserved = False
        booth.delicacy_orders.clear()

        return f"Booth {booth.booth_number}:\n" \
               f"Bill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
