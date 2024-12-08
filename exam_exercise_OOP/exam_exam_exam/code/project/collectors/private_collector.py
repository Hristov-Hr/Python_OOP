from project.collectors.base_collector import BaseCollector


class PrivateCollector(BaseCollector):

    def __init__(self, name: str):
        super().__init__(name, available_money=25000.0, available_space=3000)

    def increase_money(self):
        self.available_money += 5000.0