from project.id_mixin import IdMixin


class Equipment(IdMixin):
    id = 1

    def __init__(self, name):
        self.name = name
        self.id = self.get_next_id()
        self.increase_id()

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"