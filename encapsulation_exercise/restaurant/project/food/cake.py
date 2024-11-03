from project import Dessert


class Cake(Dessert):

    GRAMS = 250
    CALORIES = 1000
    PRICE = 5

    def __init__(self, name):
        super(Cake, self).__init__(name, price=Cake.PRICE, grams=Cake.GRAMS, calories=Cake.CALORIES)
