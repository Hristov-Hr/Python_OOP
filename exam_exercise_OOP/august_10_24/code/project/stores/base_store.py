from abc import ABC, abstractmethod
from typing import List
from project.products.base_product import BaseProduct


class BaseStore(ABC):

    def __init__(self, name: str, location: str, capacity: int):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.products: List[BaseProduct] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Store name cannot be empty!")
        self.__name = value

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value):
        if len(value) != 3 or value[1] == '':
            raise ValueError("Store location must be 3 chars long!")
        self.__location = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Store capacity must be a positive number or 0!")
        self.__capacity = value

    def get_estimated_profit(self):
        products_prices = [p.price for p in self.products]
        estimated_profit = sum(products_prices) * 0.1
        return f"Estimated future profit for {len(products_prices)} products is {estimated_profit:.2f}"

    @property
    @abstractmethod
    def store_type(self):
        ...

    def store_stats(self):
        result = [f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}",
                  self.get_estimated_profit(),
                  f"**{'Toys' if self.__class__.__name__ == 'ToyStore' else 'Furniture'} for sale:"]

        models = list(set(p.model for p in self.products))
        for m in sorted(models):
            products = [p for p in self.products if p.model == m]
            average_price = sum([p.price for p in products]) / len(products)
            result.append(f"{m}: {len(products)}pcs, average price: {average_price:.2f}")

        return "\n".join(result)