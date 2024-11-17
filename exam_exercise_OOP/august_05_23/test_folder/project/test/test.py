from project.second_hand_car import SecondHandCar
from unittest import TestCase, main


class TestSecondHandCar(TestCase):

    def setUp(self) -> None:
        self.car = SecondHandCar("Mercedes", "coupe", 100000, 40000.00)

    def test_init(self):
        self.assertEqual("Mercedes", self.car.model)
        self.assertEqual("coupe", self.car.car_type)
        self.assertEqual([], self.car.repairs)

    def test_price(self):
        self.assertEqual(40000.00, self.car.price)
        with self.assertRaises(ValueError) as c:
            self.car.price = 1
        self.assertEqual('Price should be greater than 1.0!', str(c.exception))

    def test_mileage(self):
        self.assertEqual(100000, self.car.mileage)
        with self.assertRaises(ValueError) as c:
            self.car.mileage = 100
        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(c.exception))

    def test_set_promotional_price(self):
        with self.assertRaises(ValueError) as c:
            self.car.set_promotional_price(40000.00)
        self.assertEqual('You are supposed to decrease the price!', str(c.exception))
        self.assertEqual(40000.00, self.car.price)
        self.assertEqual('The promotional price has been successfully set.', self.car.set_promotional_price(39999.99))
        self.assertEqual(39999.99, self.car.price)

    def test_need_repair(self):
        self.assertEqual('Repair is impossible!', self.car.need_repair(20000.01, "test repair"))
        self.assertEqual('Price has been increased due to repair charges.', self.car.need_repair(20000.00, "test repair"))
        self.assertEqual(60000.00, self.car.price)
        self.assertEqual(["test repair"], self.car.repairs)

    def test_gt_(self):
        other_car = SecondHandCar("Audi", "limousine", 20000, 150000)
        self.assertEqual('Cars cannot be compared. Type mismatch!', self.car.__gt__(other_car))
        car2 = SecondHandCar("Audi", "coupe", 150000, 39999.99)
        self.assertEqual(True, self.car.__gt__(car2))
        car2.price += 0.01
        self.assertEqual(False, self.car.__gt__(car2))

    def test_str_(self):
        self.assertEqual("Model Mercedes | Type coupe | Milage 100000km\n"
                         "Current price: 40000.00 | Number of Repairs: 0", self.car.__str__())


if __name__ == "__main__":
    main()
