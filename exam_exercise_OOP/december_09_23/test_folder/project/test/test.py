from collections import deque
from unittest import TestCase, main
from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):

    def setUp(self) -> None:
        self.station = RailwayStation("Central Station")

    def test_init(self):
        self.assertEqual(deque([]), self.station.arrival_trains)
        self.assertEqual(deque([]), self.station.departure_trains)

    def test_name(self):
        self.assertEqual("Central Station", self.station.name)
        with self.assertRaises(ValueError) as c:
            self.station.name = "Tst"
        self.assertEqual("Name should be more than 3 symbols!", str(c.exception))

    def test_new_arrival_on_board(self):
        self.station.new_arrival_on_board("TestArrival")
        self.assertEqual(deque(["TestArrival"]), self.station.arrival_trains)

    def test_train_has_arrived(self):
        self.station.new_arrival_on_board("TestArrival")
        self.assertEqual("There are other trains to arrive before Test.", self.station.train_has_arrived("Test"))
        self.assertEqual("TestArrival is on the platform and will leave in 5 minutes.", self.station.train_has_arrived("TestArrival"))
        self.assertEqual(deque(['TestArrival']), self.station.departure_trains)
        self.assertEqual(deque([]), self.station.arrival_trains)

    def test_train_has_left_return_true(self):
        self.station.departure_trains.append("Test")
        self.assertEqual(True, self.station.train_has_left("Test"))
        self.assertEqual(deque([]), self.station.departure_trains)

    def test_train_has_left_return_false(self):
        self.station.departure_trains.append("Test")
        self.assertEqual(False, self.station.train_has_left("Tst"))


if __name__ == "__main__":
    main()