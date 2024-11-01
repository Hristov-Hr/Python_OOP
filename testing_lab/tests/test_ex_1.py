from Python_OOP.testing_lab.test_worker import Worker

from unittest import TestCase, main


class WorkerTests(TestCase):

    def test_init_worker(self):

        worker = Worker("Test", 1000, 150)
        self.assertEqual("Test", worker.name)
        self.assertEqual(1000, worker.salary)
        self.assertEqual(150, worker.energy)
        self.assertEqual(0, worker.money)

    def test_energy_incremented(self):
        worker = Worker("Test", 1000, 150)
        worker.rest()
        self.assertEqual(151, worker.energy)

    def test_worker_raise_exception(self):
        worker = Worker("Test", 1000, 0)
        with self.assertRaises(Exception) as w:
            worker.work()

        self.assertEqual('Not enough energy.', str(w.exception))
        self.assertEqual(0, worker.money)
        self.assertEqual(0, worker.energy)

        worker = Worker("Test", 1000, -5)
        with self.assertRaises(Exception) as w:
            worker.work()

        self.assertEqual('Not enough energy.', str(w.exception))
        self.assertEqual(0, worker.money)
        self.assertEqual(-5, worker.energy)

    def test_money_increase(self):
        worker = Worker("Test", 1000, 150)
        worker.work()
        self.assertEqual(1000, worker.money)
        self.assertEqual(149, worker.energy)

    def test_get_info(self):
        worker = Worker("Test", 1000, 150)
        worker.work()
        self.assertEqual('Test has saved 1000 money.', worker.get_info())


if __name__ == "__main__":
    main()