class Customer:

    def __init__(self, name, age, id_):
        self.name = name
        self.age = age
        self.id = id_
        self.rented_dvds = []

    def __repr__(self):
        return f"{self.id}: {self.name} of age {self.age} has \
{len(self.rented_dvds)} rented DVD\'s ({', '.join(d.name for d in self.rented_dvds)})"