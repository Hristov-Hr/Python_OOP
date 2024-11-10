from project.products.base_product import BaseProduct
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.base_store import BaseStore
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore


class FactoryManager:

    VALID_PRODUCT_TYPES = {"Chair": Chair, "HobbyHorse": HobbyHorse}
    VALID_STORE_TYPES = {'FurnitureStore': FurnitureStore, 'ToyStore': ToyStore}

    def __init__(self, name):
        self.name = name
        self.income = 0.0
        self.products = []
        self.stores = []

    def produce_item(self, product_type: str, model: str, price: float):
        if product_type not in self.VALID_PRODUCT_TYPES.keys():
            raise Exception("Invalid product type!")

        product = self.VALID_PRODUCT_TYPES[product_type](model, price)
        self.products.append(product)

        return f"A product of sub-type {product.sub_type} was produced."

    def register_new_store(self, store_type: str, name: str, location: str):

        if store_type not in self.VALID_STORE_TYPES.keys():
            raise Exception(f"{store_type} is an invalid type of store!")

        store = self.VALID_STORE_TYPES[store_type](name, location)
        self.stores.append(store)

        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct):

        product_type = {'FurnitureStore': 'Furniture', 'ToyStore': 'Toys'}

        if store.capacity < len(products):
            return f"Store {store.name} has no capacity for this purchase."

        products_for_sale = [p for p in products if p.sub_type == product_type[store.__class__.__name__] and p in self.products]

        if products_for_sale:
            for pr in products_for_sale:
                store.products.append(pr)
                store.capacity -= 1
                self.products.remove(pr)
                self.income += pr.price

            return f"Store {store.name} successfully purchased {len(products_for_sale)} items."
        return "Products do not match in type. Nothing sold."

    def unregister_store(self, store_name: str):

        try:
            store = next(filter(lambda x: x.name == store_name, self.stores))
        except StopIteration:
            raise Exception("No such store!")

        if store.products:
            return "The store is still having products in stock! Unregistering is inadvisable."

        self.stores.remove(store)
        return f"Successfully unregistered store {store_name}, location: {store.location}."

    def discount_products(self, product_model: str):

        products_count = [p.discount() for p in self.products if p.model == product_model]
        return f"Discount applied to {len(products_count)} products with model: {product_model}"

    def request_store_stats(self, store_name: str):

        try:
            store = next(filter(lambda x: x.name == store_name, self.stores))
            return store.store_stats()

        except StopIteration:
            return "There is no store registered under this name!"

    def statistics(self):

        result = [f"Factory: {self.name}", f"Income: {self.income:.2f}", "***Products Statistics***",
                  f"Unsold Products: {len(self.products)}. Total net price: {sum(p.price for p in self.products):.2f}"]

        model_counter = {}
        for i in self.products:
            if i.model not in model_counter:
                model_counter[i.model] = 0
            model_counter[i.model] += 1

        for k, v in sorted(model_counter.items(), key=lambda x: x[0]):
            result.append(f"{k}: {v}")

        result.append(f"***Partner Stores: {len(self.stores)}***")

        [result.append(s.name) for s in sorted(self.stores, key=lambda x: x.name)]

        return "\n".join(result)






