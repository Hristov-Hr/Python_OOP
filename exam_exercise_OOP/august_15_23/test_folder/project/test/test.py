from project.trip import Trip
from unittest import TestCase, main


class TestTrip(TestCase):

    def setUp(self) -> None:
        self.trip = Trip(13500, 2, True)

    def test_booked_destinations_paid_amounts(self):
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)

    def test_travelers(self):
        self.assertEqual(2, self.trip.travelers)
        with self.assertRaises(ValueError) as t:
            self.trip.travelers -= 2
        self.assertEqual('At least one traveler is required!', str(t.exception))

    def test_is_family(self):
        self.assertEqual(True, self.trip.is_family)
        self.trip = Trip(3000, 1, True)
        self.assertEqual(False, self.trip.is_family)

    def test_book_trip_and_booking_status_with_budget(self):
        self.assertEqual('This destination is not in our offers, please choose a new one!', self.trip.book_a_trip("Italy"))
        self.assertEqual(f'Successfully booked destination New Zealand! Your budget left is 0.00', self.trip.book_a_trip('New Zealand'))
        self.assertEqual(0, self.trip.budget)
        self.assertEqual({'New Zealand': 13500}, self.trip.booked_destinations_paid_amounts)
        self.assertEqual("Booked Destination: New Zealand\nPaid Amount: 13500.00\nNumber of Travelers: 2\nBudget Left: 0.00", self.trip.booking_status())

    def test_book_trip_and_booking_status_without_budget(self):
        self.trip.is_family = False
        self.assertEqual('Your budget is not enough!', self.trip.book_a_trip('New Zealand'))
        self.assertEqual(13500, self.trip.budget)
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)
        self.assertEqual(f'No bookings yet. Budget: 13500.00', self.trip.booking_status())


if __name__ == "__main__":
    main()
