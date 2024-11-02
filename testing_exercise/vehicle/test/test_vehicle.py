from project.vehicle import Vehicle
from unittest import TestCase, main


class TestVehicle(TestCase):

    def test_class_var(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def setUp(self) -> None:
        self.vehicle = Vehicle(75.0, 240.0)

    def test_init(self):
        self.assertIsInstance(self.vehicle.fuel, float)
        self.assertIsInstance(self.vehicle.horse_power, float)
        self.assertEqual(self.vehicle.fuel_consumption, Vehicle.DEFAULT_FUEL_CONSUMPTION)
        self.assertEqual(self.vehicle.fuel, self.vehicle.capacity)
        self.assertGreater(self.vehicle.capacity, 0)
        self.assertGreater(self.vehicle.horse_power, 0)

    def test_drive(self):
        with self.assertRaises(Exception) as v:
            self.vehicle.drive(61)
        self.assertEqual("Not enough fuel", str(v.exception))

        self.vehicle.drive(10)
        self.assertEqual(62.5, self.vehicle.fuel)
        self.vehicle.drive(50)
        self.assertEqual(0, self.vehicle.fuel)

    def test_refuel(self):
        self.vehicle.fuel = 10
        self.vehicle.refuel(65)
        self.assertEqual(75, self.vehicle.fuel)
        with self.assertRaises(Exception) as v:
            self.vehicle.refuel(1)
        self.assertEqual("Too much fuel", str(v.exception))
        self.assertEqual(75.0, self.vehicle.fuel)

    def test_string(self):
        result = str(self.vehicle)
        self.assertEqual("The vehicle has 240.0 horse power with 75.0 fuel left and 1.25 fuel consumption", result)


if __name__ == '__main__':
    main()
