class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__animal_capacity == len(self.animals):
            return "Not enough space for animal"
        if price > self.__budget:
            return "Not enough budget"
        self.__budget -= price
        self.animals.append(animal)
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if self.__workers_capacity == len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        try:
            worker = next(filter(lambda w: worker_name == w.name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"
        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        total_salary = sum(w.salary for w in self.workers)
        if self.__budget < total_salary:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= total_salary
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        total_amount_for_care = sum(a.money_for_care for a in self.animals)
        if self.__budget < total_amount_for_care:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= total_amount_for_care
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [x for x in self.animals if x.__class__.__name__ == 'Lion']
        tigers = [x for x in self.animals if x.__class__.__name__ == 'Tiger']
        cheetahs = [x for x in self.animals if x.__class__.__name__ == 'Cheetah']

        result = f"You have {len(self.animals)} animals\n----- {len(lions)} Lions:\n"

        for lion in lions:
            result += f"{lion}\n"

        result += f"----- {len(tigers)} Tigers:\n"

        for tiger in tigers:
            result += f"{tiger}\n"

        result += f"----- {len(cheetahs)} Cheetahs:\n"

        for cheetah in cheetahs:
            result += f"{cheetah}\n"

        return result.strip()

    def workers_status(self):
        keepers = [x for x in self.workers if x.__class__.__name__ == 'Keeper']
        caretakers = [x for x in self.workers if x.__class__.__name__ == 'Caretaker']
        vets = [x for x in self.workers if x.__class__.__name__ == 'Vet']

        result = f"You have {len(self.workers)} workers\n----- {len(keepers)} Keepers:\n"

        for keeper in keepers:
            result += f"{keeper}\n"

        result += f"----- {len(caretakers)} Caretakers:\n"

        for caretaker in caretakers:
            result += f"{caretaker}\n"

        result += f"----- {len(vets)} Vets:\n"

        for vet in vets:
            result += f"{vet}\n"

        return result.strip()

