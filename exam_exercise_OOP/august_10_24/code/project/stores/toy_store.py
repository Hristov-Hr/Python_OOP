from project.stores.base_store import BaseStore


class ToyStore(BaseStore):

    def __init__(self, name: str, location: str):
        super().__init__(name, location, capacity=100)

    @property
    def store_type(self):
        return "ToyStore"