from Python_OOP.testing_lab.car_manager import Car
from unittest import TestCase, main


class TestCar(TestCase):

    def setUp(self) -> None:
        self.car = Car("Porsche", 911, 10, 80)

    def test_init(self):
        self.assertEqual("Porsche", self.car.make)
        self.assertEqual(911, self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(80, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_set_make_with_empty_string(self):
        with self.assertRaises(Exception) as c:
            self.car.make = ""
        self.assertEqual("Make cannot be null or empty!", str(c.exception))

    def test_set_model_with_empty_string(self):
        with self.assertRaises(Exception) as c:
            self.car.model = ""
        self.assertEqual("Model cannot be null or empty!", str(c.exception))

    def test_set_fuel_consumption_to_zero_or_negative(self):
        with self.assertRaises(Exception) as c:
            self.car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(c.exception))

        with self.assertRaises(Exception) as c:
            self.car.fuel_consumption = -1
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(c.exception))

    def test_set_fuel_capacity_to_zero_or_negative(self):
        with self.assertRaises(Exception) as c:
            self.car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(c.exception))

        with self.assertRaises(Exception) as c:
            self.car.fuel_capacity = -1
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(c.exception))

    def test_set_fuel_amount_to_negative(self):
        with self.assertRaises(Exception) as c:
            self.car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(c.exception))

    def test_refuel(self):
        with self.assertRaises(Exception) as c:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(c.exception))

        with self.assertRaises(Exception) as c:
            self.car.refuel(-1)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(c.exception))

        self.car.refuel(1)
        self.assertEqual(1, self.car.fuel_amount)
        self.car.refuel(80)
        self.assertEqual(80, self.car.fuel_amount)

    def test_drive(self):
        self.car.refuel(50)
        self.car.drive(500)
        self.assertEqual(0, self.car.fuel_amount)
        self.car.refuel(50)
        self.car.drive(450)
        self.assertEqual(5, self.car.fuel_amount)
        with self.assertRaises(Exception) as c:
            self.car.drive(51)
        self.assertEqual("You don't have enough fuel to drive!", str(c.exception))


if __name__ == "__main__":
    main()