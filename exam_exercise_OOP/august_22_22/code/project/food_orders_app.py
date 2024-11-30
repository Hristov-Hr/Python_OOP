from typing import List

from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:

    VALID_MEALS = {"Starter": Starter, "MainDish": MainDish, "Dessert": Dessert}
    ID_COUNTER = 0

    def __init__(self):
        self.menu: List[Meal] = []
        self.clients_list: List[Client] = []

    def register_client(self, client_phone_number: str):
        try:
            next(filter(lambda x: client_phone_number == x.phone_number, self.clients_list))
            raise Exception("The client has already been registered!")

        except StopIteration:
            self.clients_list.append(Client(client_phone_number))
            return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):

        [self.menu.append(m) for m in meals if m.MEAL_TYPE in self.VALID_MEALS]

    def show_menu(self):
        result = [m.details() for m in self.menu]

        if len(result) < 5:
            raise Exception("The menu is not ready!")

        return "\n".join(result)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        try:
            client = next(filter(lambda x: client_phone_number == x.phone_number, self.clients_list))
        except StopIteration:
            client = self.register_client(client_phone_number)

        for_order = []
        amount = 0
        for m, q in meal_names_and_quantities.items():
            try:
                meal = next(filter(lambda x: x.name == m, self.menu))
                if meal.quantity < q:
                    raise Exception(f"Not enough quantity of {meal.MEAL_TYPE}: {meal.name}!")
                for_order.append(meal)
                amount += meal.price * q
            except StopIteration:
                raise Exception(f"{m} is not on the menu!")

        client.bill += amount
        client.shopping_cart.extend(for_order)

        for k, v in meal_names_and_quantities.items():
            product = [p for p in self.menu if p.name == k][0]
            product.quantity -= v
            client.order[product.name] = product.quantity

        return f"Client {client_phone_number} successfully ordered {', '.join([m.name for m in client.shopping_cart])} " \
               f"for {amount}lv."

    def cancel_order(self, client_phone_number: str):

        client = next(filter(lambda x: client_phone_number == x.phone_number, self.clients_list))

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        client.bill = 0.0

        for k, v in client.order.items():
            meal = next(filter(lambda x: k == x.name, self.menu))
            meal.quantity += v

        return f"Client {client.phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):

        client = next(filter(lambda x: client_phone_number == x.phone_number, self.clients_list))

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        total_paid_money = client.bill
        client.bill = 0.0
        client.shopping_cart.clear()
        self.ID_COUNTER += 1

        return f"Receipt #{self.ID_COUNTER} with total amount of {total_paid_money:.2f} " \
               f"was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
