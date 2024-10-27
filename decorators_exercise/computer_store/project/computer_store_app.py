from computer_types.desktop_computer import DesktopComputer
from computer_types.laptop import Laptop


class ComputerStoreApp:

    valid_computers = {"Desktop Computer": DesktopComputer, "Laptop": Laptop}

    def __init__(self):
        self.warehouse = []
        self.profits = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        try:
            computer = self.valid_computers[type_computer](manufacturer, model)
        except KeyError:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        configuration = computer.configure_computer(processor, ram)
        self.warehouse.append(computer)

        return configuration

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        for comp in self.warehouse:
            if comp.price <= client_budget and comp.processor == wanted_processor and comp.ram >= wanted_ram:
                self.profits += client_budget - comp.price
                self.warehouse.remove(comp)
                return f"{comp} sold for {client_budget}$."

        raise Exception("Sorry, we don't have a computer for you.")


