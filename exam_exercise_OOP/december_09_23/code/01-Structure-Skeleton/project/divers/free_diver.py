from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    OXYGEN_LEVEL_VALUE = 120.0

    def __init__(self, name):
        super().__init__(name, oxygen_level=self.OXYGEN_LEVEL_VALUE)

    def miss(self, time_to_catch: int):
        value = time_to_catch * 0.6
        if self.oxygen_level > value:
            self.oxygen_level -= value
        else:
            self.oxygen_level = 0
        self.check_health()
