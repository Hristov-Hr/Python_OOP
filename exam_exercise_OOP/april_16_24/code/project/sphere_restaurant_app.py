from typing import List

from project.clients.base_client import BaseClient
from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient
from project.waiters.base_waiter import BaseWaiter
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:

    VALID_WAITER_TYPE = {"FullTimeWaiter": FullTimeWaiter, "HalfTimeWaiter": HalfTimeWaiter}
    VALID_CLIENT_TYPE = {"RegularClient": RegularClient, "VIPClient": VIPClient}

    def __init__(self):
        self.waiters: List[BaseWaiter] = []
        self.clients: List[BaseClient] = []

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int):

        if waiter_type not in self.VALID_WAITER_TYPE.keys():
            return f"{waiter_type} is not a recognized waiter type."

        try:
            next(filter(lambda x: x.name == waiter_name, self.waiters))
            return f"{waiter_name} is already on the staff."

        except StopIteration:
            self.waiters.append(self.VALID_WAITER_TYPE[waiter_type](waiter_name, hours_worked))
            return f"{waiter_name} is successfully hired as a {waiter_type}."

    def admit_client(self, client_type: str, client_name: str):

        if client_type not in self.VALID_CLIENT_TYPE.keys():
            return f"{client_type} is not a recognized client type."

        try:
            next(filter(lambda x: x.name == client_name, self.clients))
            return f"{client_name} is already a client."

        except StopIteration:
            self.clients.append(self.VALID_CLIENT_TYPE[client_type](client_name))
            return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name: str):
        try:
            waiter = next(filter(lambda x: x.name == waiter_name, self.waiters))
            return waiter.report_shift()

        except StopIteration:
            return f"No waiter found with the name {waiter_name}."

    def process_client_order(self, client_name: str, order_amount: float):
        try:
            client = next(filter(lambda x: x.name == client_name, self.clients))
            points_earned = client.earning_points(order_amount)
            return f"{client_name} earned {points_earned} points from the order."

        except StopIteration:
            return f"{client_name} is not a registered client."

    def apply_discount_to_client(self, client_name: str):
        try:
            client = next(filter(lambda x: x.name == client_name, self.clients))
            discount_percentage, remaining_points = client.apply_discount()
            return f"{client_name} received a {discount_percentage}% discount. Remaining points {remaining_points}"

        except StopIteration:
            return f"{client_name} cannot get a discount because this client is not admitted!"

    def generate_report(self):

        total_earnings = sum(w.calculate_earnings() for w in self.waiters)
        total_client_points = sum(c.points for c in self.clients)

        result = ["$$ Monthly Report $$", f"Total Earnings: ${total_earnings:.2f}",
                  f"Total Clients Unused Points: {total_client_points}", f"Total Clients Count: {len(self.clients)}",
                  "** Waiter Details **"]

        [result.append(str(w)) for w in sorted(self.waiters, key=lambda x: -x.calculate_earnings())]

        return "\n".join(result)
