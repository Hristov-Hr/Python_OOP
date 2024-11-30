from project.meals.meal import Meal


class MainDish(Meal):

    MEAL_TYPE = "MainDish"

    def __init__(self, name: str, price: float, quantity=50):
        super().__init__(name, price, quantity)

    def details(self):
        return f"MainDish {self.name}: {self.price:.2f}lv/piece"