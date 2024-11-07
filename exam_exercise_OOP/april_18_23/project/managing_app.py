from project.route import Route
from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:

    VALID_VEHICLE_TYPE = {"PassengerCar": PassengerCar, "CargoVan": CargoVan}

    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        try:
            next(filter(lambda x: x.driving_license_number == driving_license_number, self.users))
            return f"{driving_license_number} has already been registered to our platform."
        except StopIteration:
            self.users.append(User(first_name, last_name, driving_license_number))
            return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):

        try:
            vehicle = self.VALID_VEHICLE_TYPE[vehicle_type](brand, model, license_plate_number)
        except KeyError:
            return f"Vehicle type {vehicle_type} is inaccessible."

        try:
            next(filter(lambda x: x.license_plate_number == license_plate_number, self.vehicles))
            return f"{license_plate_number} belongs to another vehicle."

        except StopIteration:
            self.vehicles.append(vehicle)
            return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        try:
            route = next(filter(lambda x: x.start_point == start_point and x.end_point == end_point, self.routes))
            if route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
            if route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
            route.is_locked = True
            return self.create_route(start_point, end_point, length)

        except StopIteration:
            return self.create_route(start_point, end_point, length)

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int, is_accident_happened):
        user = next(filter(lambda x: x.driving_license_number == driving_license_number, self.users))
        vehicle = next(filter(lambda x: x.license_plate_number == license_plate_number, self.vehicles))
        route = next(filter(lambda x: x.route_id == route_id, self.routes))

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()

        else:
            user.increase_rating()

        return str(vehicle)

    def repair_vehicles(self, count: int):
        damaged_vehicles = [v for v in self.vehicles if v.is_damaged is True]
        sorted_vehicles = sorted(damaged_vehicles, key=lambda x: (x.brand, x.model))[:count]
        for veh in sorted_vehicles:
            veh.recharge()
            veh.change_status()

        return f"{len(sorted_vehicles)} vehicles were successfully repaired!"

    def users_report(self):
        result = ["*** E-Drive-Rent ***"]
        [result.append(str(u)) for u in sorted(self.users, key=lambda x: -x.rating)]

        return "\n".join(result)

    def create_route(self, start, end, length):
        next_id = len(self.routes) + 1
        self.routes.append(Route(start, end, length, next_id))
        return f"{start}/{end} - {length} km is unlocked and available to use."
