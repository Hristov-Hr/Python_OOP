from abc import ABC, abstractmethod


class BaseVehicle(ABC):

    def __init__(self, brand: str, model: str, license_plate_number: str, max_mileage: float):
        self.brand = brand
        self.model = model
        self.license_plate_number = license_plate_number
        self.max_mileage = max_mileage
        self.battery_level: int = 100
        self.is_damaged: bool = False

    @abstractmethod
    def drive(self, mileage: float):
        ...

    def recharge(self):
        self.battery_level = 100

    def change_status(self):
        self.is_damaged = -self.is_damaged

    def __str__(self):
        status = "Damaged" if self.is_damaged else "OK"
        return f"{self.brand} {self.model} License plate: {self.license_plate_number} Battery: {self.battery_level}% Status: {status}"



