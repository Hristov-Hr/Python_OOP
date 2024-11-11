from unittest import TestCase, main

from project.restaurant import Restaurant


class TestRestaurant(TestCase):

    def setUp(self) -> None:
        self.restaurant = Restaurant("Casablanca", 2)

    def test_init(self):
        self.assertEqual("Casablanca", self.restaurant.name)
        self.assertEqual(2, self.restaurant.capacity)
        self.assertEqual([], self.restaurant.waiters)

    def test_name(self):
        self.assertEqual("Casablanca", self.restaurant.name)
        with self.assertRaises(ValueError) as r:
            self.restaurant.name = " "
        self.assertEqual("Invalid name!", str(r.exception))

    def test_capacity(self):
        self.restaurant.capacity -= 2
        self.assertEqual(0, self.restaurant.capacity)
        with self.assertRaises(ValueError) as r:
            self.restaurant.capacity -= 1
        self.assertEqual("Invalid capacity!", str(r.exception))

    def test_add_and_remove_waiter(self):
        self.assertEqual("The waiter Peter has been added.", self.restaurant.add_waiter("Peter"))
        self.assertEqual([{'name': 'Peter'}], self.restaurant.waiters)
        self.assertEqual("The waiter Peter already exists!", self.restaurant.add_waiter("Peter"))
        self.assertEqual([{'name': 'Peter'}], self.restaurant.waiters)
        self.assertEqual("The waiter Ivan has been added.", self.restaurant.add_waiter("Ivan"))
        self.assertEqual([{'name': 'Peter'}, {'name': 'Ivan'}], self.restaurant.waiters)
        self.assertEqual("No more places!", self.restaurant.add_waiter("George"))
        self.assertEqual([{'name': 'Peter'}, {'name': 'Ivan'}], self.restaurant.waiters)
        self.assertEqual("No waiter found with the name George.", self.restaurant.remove_waiter("George"))
        self.assertEqual([{'name': 'Peter'}, {'name': 'Ivan'}], self.restaurant.waiters)
        self.assertEqual("The waiter Ivan has been removed.", self.restaurant.remove_waiter("Ivan"))
        self.assertEqual([{'name': 'Peter'}], self.restaurant.waiters)

    def test_get_waiter_without_earning(self):
        self.restaurant.waiters = [{'name': 'Peter'}, {'name': 'Ivan'}]
        self.assertEqual([{'name': 'Peter'}, {'name': 'Ivan'}], self.restaurant.get_waiters())
        self.assertEqual([], self.restaurant.get_waiters(1, 5))

    def test_get_waiter_with_earning(self):
        self.restaurant.waiters = [{'name': 'Peter', 'total_earnings': 1}, {'name': 'Ivan', 'total_earnings': 5}]
        self.assertEqual([], self.restaurant.get_waiters(2, 4))
        self.assertEqual([{'name': 'Peter', 'total_earnings': 1}, {'name': 'Ivan', 'total_earnings': 5}], self.restaurant.get_waiters(1, 5))

    def test_get_total_earnings(self):
        self.assertEqual(0, self.restaurant.get_total_earnings())
        self.restaurant.waiters = [{'name': 'Peter', 'total_earnings': 1}, {'name': 'Ivan', 'total_earnings': 5}]
        self.assertEqual(6, self.restaurant.get_total_earnings())


if __name__ == "__main__":
    main()