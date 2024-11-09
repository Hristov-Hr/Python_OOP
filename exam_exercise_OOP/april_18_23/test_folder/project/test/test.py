from project.robot import Robot
from unittest import TestCase, main


class TestRobot(TestCase):

    def test_class_attributes(self):

        self.assertEqual(1.5, Robot.PRICE_INCREMENT)
        self.assertEqual(sorted(['Military', 'Education', 'Entertainment', 'Humanoids']), sorted(Robot.ALLOWED_CATEGORIES))

    def setUp(self):
        self.robot = Robot("Test_id", 'Military', 100, 500.00)

    def test_init(self):
        self.assertIsInstance(self.robot.robot_id, str)
        self.assertIsInstance(self.robot.category, str)
        self.assertIsInstance(self.robot.available_capacity, int)
        self.assertIsInstance(self.robot.price, float)
        self.assertEqual([], self.robot.software_updates)
        self.assertEqual([], self.robot.hardware_upgrades)

    def test_category(self):
        self.assertEqual('Military', self.robot.category)
        with self.assertRaises(ValueError) as r:
            self.robot.category = "military"
        self.assertEqual(f"Category should be one of '{self.robot.ALLOWED_CATEGORIES}'", str(r.exception))

    def test_price(self):
        self.robot.price = 0
        self.assertEqual(0, self.robot.price)
        with self.assertRaises(ValueError) as r:
            self.robot.price -= 1
        self.assertEqual("Price cannot be negative!", str(r.exception))

    def test_upgrade(self):
        self.assertEqual('Robot Test_id was upgraded with camera.', self.robot.upgrade("camera", 50))
        self.assertEqual(["camera"], self.robot.hardware_upgrades)
        self.assertEqual(575, self.robot.price)
        self.assertEqual("Robot Test_id was not upgraded.", self.robot.upgrade("camera", 50))
        self.assertEqual(["camera"], self.robot.hardware_upgrades)
        self.assertEqual(575, self.robot.price)

    def test_update(self):
        self.assertEqual(f'Robot Test_id was updated to version 5.2.', self.robot.update(5.2, 64))
        self.assertEqual([5.2], self.robot.software_updates)
        self.assertEqual(36, self.robot.available_capacity)
        self.assertEqual("Robot Test_id was not updated.", self.robot.update(5.3, 64))
        self.assertEqual([5.2], self.robot.software_updates)
        self.assertEqual(36, self.robot.available_capacity)
        self.assertEqual("Robot Test_id was not updated.", self.robot.update(5.2, 4))
        self.assertEqual([5.2], self.robot.software_updates)
        self.assertEqual(36, self.robot.available_capacity)
        self.assertEqual(f'Robot Test_id was updated to version 5.3.', self.robot.update(5.3, 36))
        self.assertEqual([5.2, 5.3], self.robot.software_updates)
        self.assertEqual(0, self.robot.available_capacity)

    def test_gt(self):
        other_robot = Robot("Other", 'Education', 100, 499.99)
        self.assertEqual('Robot with ID Test_id is more expensive than Robot with ID Other.', self.robot.__gt__(other_robot))
        other_robot.price += 0.01
        self.assertEqual('Robot with ID Test_id costs equal to Robot with ID Other.', self.robot.__gt__(other_robot))
        other_robot.price += 0.01
        self.assertEqual("Robot with ID Test_id is cheaper than Robot with ID Other.", self.robot.__gt__(other_robot))


if __name__ == "__main__":
    main()