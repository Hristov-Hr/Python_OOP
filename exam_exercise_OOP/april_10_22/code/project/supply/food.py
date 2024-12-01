from project.supply.supply import Supply


class Food(Supply):
    SUPPLY_TYPE = "Food"

    def __init__(self, name, energy=25):
        super().__init__(name, energy)

    def details(self):
        return f"Food: {self.name}, {self.energy}"