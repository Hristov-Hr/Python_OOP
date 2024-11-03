from abc import ABC, abstractmethod

from project import Food


class Animal(ABC):

    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass

    def feed(self, food: Food):
        food_specification = {
            "Owl": [0.25, "Meat"],
            "Hen": [0.35, "Vegetable", "Fruit", "Meat", "Seed"],
            "Mouse": [0.1, "Vegetable", "Fruit"],
            "Dog": [0.4, "Meat"],
            "Cat": [0.3, "Meat", "Vegetable"],
            "Tiger": [1, "Meat"]
        }
        if food.__class__.__name__ not in food_specification[self.__class__.__name__]:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += food.quantity * food_specification[self.__class__.__name__][0]


class Bird(Animal, ABC):

    def __init__(self, name, weight, wing_size):
        super(Bird, self).__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"