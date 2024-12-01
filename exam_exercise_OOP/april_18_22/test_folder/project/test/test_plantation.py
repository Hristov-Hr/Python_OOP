from project.plantation import Plantation
from unittest import TestCase, main


class TestPlantation(TestCase):

    def setUp(self) -> None:
        self.plantation = Plantation(10)

    def test__init__(self):
        self.assertEqual(self.plantation.size, 10)
        self.assertEqual(self.plantation.plants, {})
        self.assertEqual(self.plantation.workers, [])

    def test_size_setter(self):
        with self.assertRaises(ValueError) as pl:
            self.plantation.size = -1
        self.assertEqual("Size must be positive number!", str(pl.exception))

    def test_hire_worker(self):
        self.assertEqual("worker successfully hired.", self.plantation.hire_worker("worker"))
        self.assertEqual(["worker"], self.plantation.workers)
        with self.assertRaises(ValueError) as pl:
            self.plantation.hire_worker("worker")
        self.assertEqual("Worker already hired!", str(pl.exception))
        self.assertEqual(["worker"], self.plantation.workers)

    def test__len__(self):
        self.assertEqual(0, self.plantation.__len__())
        self.plantation.plants = {"plant": ["1", "2", "3"], "plant2": ["1", "2"]}
        self.assertEqual(5, self.plantation.__len__())

    def test_error_planting(self):
        with self.assertRaises(ValueError) as pl:
            self.plantation.planting("worker", "plant")
        self.assertEqual("Worker with name worker is not hired!", str(pl.exception))

        with self.assertRaises(ValueError) as pl:
            self.plantation.plants = {"plant": ["1", "2", "3", "4", "5", "6", "7", "8"], "plant2": ["1", "2"]}
            self.plantation.workers = ["worker"]
            self.plantation.planting("worker", "plant3")
        self.assertEqual(str(pl.exception), "The plantation is full!")

    def test_planting(self):
        self.plantation.workers = ["worker"]
        self.assertEqual("worker planted it's first plant.", self.plantation.planting("worker", "plant"))
        self.assertEqual(self.plantation.plants, {"worker": ["plant"]})
        self.assertEqual(self.plantation.planting("worker", "plant2"), "worker planted plant2.")
        self.assertEqual(self.plantation.plants, {"worker": ["plant", "plant2"]})
        self.plantation.hire_worker("worker2")
        self.assertEqual("worker2 planted it's first plant.", self.plantation.planting("worker2", "plant"))
        self.assertEqual(self.plantation.plants, {"worker": ["plant", "plant2"], "worker2": ["plant"]})

    def test__str__(self):
        self.plantation.workers = ["worker", "worker2"]
        self.plantation.plants = {"worker": ["plant", "plant2"], "worker2": ["plant"]}
        result = ["Plantation size: 10", "worker, worker2", "worker planted: plant, plant2", "worker2 planted: plant"]
        self.assertEqual('\n'.join(result), self.plantation.__str__())

    def test__repr__(self):
        self.plantation.workers = ["worker", "worker2"]
        result = 'Size: 10\n' + 'Workers: worker, worker2'
        self.assertEqual(result, self.plantation.__repr__())


if __name__ == "__main__":
    main()