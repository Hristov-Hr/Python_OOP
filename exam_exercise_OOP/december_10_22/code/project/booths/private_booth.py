from project.booths.booth import Booth


class PrivateBooth(Booth):

    def reserve(self, number_of_people: int):
        self.price_for_reservation = number_of_people * 3.50
        self.is_reserved = True