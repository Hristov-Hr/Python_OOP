from project.supply.supply import Supply


class Drink(Supply):
    SUPPLY_TYPE = "Drink"

    def __init__(self, name, energy=15):
        super().__init__(name, energy)

    def details(self):
        return f"Drink: {self.name}, {self.energy}"