from project.delicacies.delicacy import Delicacy


class Stolen(Delicacy):

    def __init__(self, name: str, price: float):
        super().__init__(name, price, portion=250)

    def details(self):
        return f"Stolen {self.name}: 250g - {self.price:.2f}lv."
