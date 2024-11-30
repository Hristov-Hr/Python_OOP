from unittest import TestCase, main

from project.climbing_robot import ClimbingRobot


class TestClimbingRobot(TestCase):

    def setUp(self) -> None:
        self.robot = ClimbingRobot("Mountain", "test", 10, 4)

    def test_class_attributes(self):
        self.assertEqual(['Mountain', 'Alpine', 'Indoor', 'Bouldering'], self.robot.ALLOWED_CATEGORIES)

    def test__init__(self):
        self.assertEqual('Mountain', self.robot.category)
        self.assertEqual(self.robot.memory, 4)
        self.assertEqual(self.robot.capacity, 10)
        self.assertEqual(self.robot.part_type, "test")
        self.assertEqual(self.robot.installed_software, [])

    def test_category_setter(self):
        with self.assertRaises(ValueError) as r:
            self.robot.category = "aaa"
        self.assertEqual(str(r.exception), f"Category should be one of {self.robot.ALLOWED_CATEGORIES}")

    def test_get_used_capacity_and_test_get_available_capacity(self):
        self.robot.install_software({"name": "Test", 'capacity_consumption': 2, 'memory_consumption': 2})
        self.robot.install_software({"name": "Test2", 'capacity_consumption': 1, 'memory_consumption': 1})

        self.assertEqual(self.robot.get_used_capacity(), 3)
        self.assertEqual(self.robot.get_available_capacity(), 7)

    def test_get_used_memory_and_get_available_memory(self):
        self.robot.install_software({"name": "Test", 'capacity_consumption': 2, 'memory_consumption': 2})
        self.robot.install_software({"name": "Test2", 'capacity_consumption': 1, 'memory_consumption': 1})

        self.assertEqual(self.robot.get_used_memory(), 3)
        self.assertEqual(self.robot.get_available_memory(), 1)

    def test_install_software(self):
        self.assertEqual("Software 'Test' successfully installed on Mountain part.",
                         self.robot.install_software({"name": "Test", 'capacity_consumption': 2,
                                                      'memory_consumption': 2}))
        self.assertEqual(self.robot.installed_software, [{"name": "Test", 'capacity_consumption': 2,
                                                          'memory_consumption': 2}])

        self.assertEqual("Software 'Test2' cannot be installed on Mountain part.",
                         self.robot.install_software({"name": "Test2", 'capacity_consumption': 2,
                                                      'memory_consumption': 3}))
        self.assertEqual(self.robot.installed_software, [{"name": "Test", 'capacity_consumption': 2,
                                                          'memory_consumption': 2}])

        self.assertEqual("Software 'Test2' cannot be installed on Mountain part.",
                         self.robot.install_software({"name": "Test2", 'capacity_consumption': 9,
                                                      'memory_consumption': 2}))

        self.assertEqual("Software 'Test2' successfully installed on Mountain part.",
                         self.robot.install_software({"name": "Test2", 'capacity_consumption': 8,
                                                      'memory_consumption': 2}))
        self.assertEqual(self.robot.installed_software, [{"name": "Test", 'capacity_consumption': 2,
                                                          'memory_consumption': 2}, {"name": "Test2",
                                                                                     'capacity_consumption': 8,
                                                                                     'memory_consumption': 2}])


if __name__ == "__main__":
    main()