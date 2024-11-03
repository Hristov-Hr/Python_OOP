from project import Person
from project import Employee
class Teacher(Person, Employee):

    def teach(self):
        return "teaching..."


