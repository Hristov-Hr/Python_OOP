from abc import ABC, abstractmethod
from math import log2


class Computer(ABC):

    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    @abstractmethod
    def type(self):
        pass

    @property
    @abstractmethod
    def valid_processor(self):
        ...

    @property
    @abstractmethod
    def max_ram(self):
        pass

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if not value.strip():
            raise ValueError("Manufacturer name cannot be empty.")
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if not value.strip():
            raise ValueError("Model name cannot be empty.")
        self.__model = value

    def power_of_two(self, ram):
        result = log2(ram)
        return result.is_integer()

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.valid_processor:
            raise ValueError(f"{processor} is not compatible with {self.type} {self.manufacturer} {self.model}!")
        if ram > self.max_ram or not self.power_of_two(ram):
            raise ValueError(f"{ram}GB RAM is not compatible with {self.type} {self.manufacturer} {self.model}!")
        self.processor = processor
        self.ram = ram
        self.price += self.valid_processor[processor]
        self.price += int(log2(ram)) * 100
        return f"Created {self.__repr__()} for {self.price}$."

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"