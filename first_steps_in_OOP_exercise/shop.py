class Shop:

    def __init__(self, name, items):
        self.name = name
        self.items = items

    def get_items_count(self):
        number_of_product = len(self.items)
        return number_of_product


shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
print(shop.get_items_count())
