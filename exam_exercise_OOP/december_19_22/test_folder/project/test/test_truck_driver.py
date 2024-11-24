from project.truck_driver import TruckDriver

from unittest import TestCase, main


class TestTruckDriver(TestCase):

    def setUp(self) -> None:

        self.driver = TruckDriver("Peter", 1.20)

    def test_init_(self):

        self.assertEqual("Peter", self.driver.name)
        self.assertEqual(1.20, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

    def test_earned_money(self):
        with self.assertRaises(ValueError) as d:
            self.driver.earned_money -= 1
        self.assertEqual("Peter went bankrupt.", str(d.exception))

    def test_add_cargo_offer(self):
        self.assertEqual(f"Cargo for 10 to test was added as an offer.", self.driver.add_cargo_offer("test", 10))
        self.assertEqual({"test": 10}, self.driver.available_cargos)
        with self.assertRaises(Exception) as d:
            self.driver.add_cargo_offer("test", 20)
        self.assertEqual("Cargo offer is already added.", str(d.exception))
        self.assertEqual({"test": 10}, self.driver.available_cargos)

    def test_drive_best_cargo_offer(self):

        self.driver.add_cargo_offer("test", 10)
        self.driver.add_cargo_offer("test2", 20)
        self.assertEqual(f"Peter is driving 20 to test2.", self.driver.drive_best_cargo_offer())
        self.assertEqual(24, self.driver.earned_money)
        self.assertEqual(20, self.driver.miles)

    def test_bankrupt(self):
        self.driver.money_per_mile = 0.08
        self.driver.add_cargo_offer("test", 250)
        self.driver.drive_best_cargo_offer()
        self.assertEqual(self.driver.earned_money, 0)
        self.driver.money_per_mile -= 0.01
        with self.assertRaises(ValueError) as d:
            self.driver.drive_best_cargo_offer()
        self.assertEqual(str(d.exception), "Peter went bankrupt.")

    def test_drive_best_cargo_invalid(self):
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual(result, "There are no offers available.")

    def test_check_for_activities(self):
        self.driver.earned_money = 11750
        self.driver.check_for_activities(10000)
        self.assertEqual(0, self.driver.earned_money)

    def test_eat(self):
        self.driver.earned_money = 10000
        self.driver.eat(249)
        self.assertEqual(self.driver.earned_money, 10000)
        self.driver.eat(250)
        self.assertEqual(self.driver.earned_money, 9980)
        self.driver.eat(500)
        self.assertEqual(self.driver.earned_money, 9960)

    def test_sleep(self):
        self.driver.earned_money = 10000
        self.driver.sleep(999)
        self.assertEqual(self.driver.earned_money, 10000)
        self.driver.sleep(1000)
        self.assertEqual(self.driver.earned_money, 9955)
        self.driver.sleep(2000)
        self.assertEqual(self.driver.earned_money, 9910)

    def test_pump_gas(self):
        self.driver.earned_money = 10000
        self.driver.pump_gas(1499)
        self.assertEqual(self.driver.earned_money, 10000)
        self.driver.pump_gas(1500)
        self.assertEqual(self.driver.earned_money, 9500)
        self.driver.pump_gas(3000)
        self.assertEqual(self.driver.earned_money, 9000)

    def test_repair_truck(self):
        self.driver.earned_money = 15000
        self.driver.repair_truck(9999)
        self.assertEqual(self.driver.earned_money, 15000)
        self.driver.repair_truck(10000)
        self.assertEqual(self.driver.earned_money, 7500)
        self.driver.repair_truck(20000)
        self.assertEqual(self.driver.earned_money, 0)

    def test_repr_(self):
        self.assertEqual("Peter has 0 miles behind his back.", self.driver.__repr__())


if __name__ == "__main__":
    main()