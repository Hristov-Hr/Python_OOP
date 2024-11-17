from abc import ABC, abstractmethod


class BaseProduct(ABC):

    def __init__(self, model: str, price: float, material: str, sub_type: str):
        self.model = model
        self.price = price
        self.material = material
        self.sub_type = sub_type

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if not value.strip() or len(value) < 3:
            raise ValueError("Product model must be at least 3 chars long!")
        self.__model = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Product price must be greater than zero!")
        self.__price = value

    @abstractmethod
    def discount(self):
        ...