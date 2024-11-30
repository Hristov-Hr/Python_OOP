from project.bookstore import Bookstore
from unittest import TestCase, main


class TestBookstore(TestCase):

    def setUp(self) -> None:
        self.store = Bookstore(20)

    def test__init__(self):
        self.assertEqual(20, self.store.books_limit)
        self.assertEqual({}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(0, self.store.total_sold_books)

    def test_limit_setter(self):
        with self.assertRaises(ValueError) as s:
            self.store.books_limit = 0
        self.assertEqual("Books limit of 0 is not valid", str(s.exception))

    def test__len__(self):
        self.assertEqual(0, self.store.__len__())
        self.store.receive_book("test", 2)
        self.store.receive_book("test2", 3)
        self.assertEqual(5, self.store.__len__())

    def test_receive_book(self):
        self.store.receive_book("test", 2)
        self.assertEqual("5 copies of test are available in the bookstore.", self.store.receive_book("test", 3))
        self.assertEqual({"test": 5}, self.store.availability_in_store_by_book_titles)
        self.assertEqual("15 copies of test2 are available in the bookstore.", self.store.receive_book("test2", 15))
        self.assertEqual({"test": 5, "test2": 15}, self.store.availability_in_store_by_book_titles)
        with self.assertRaises(Exception) as s:
            self.store.receive_book("test3", 1)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(s.exception))

    def test_sell_book(self):
        with self.assertRaises(Exception) as s:
            self.store.sell_book("test", 5)
        self.assertEqual("Book test doesn't exist!", str(s.exception))

        self.store.receive_book("test", 5)
        with self.assertRaises(Exception) as s:
            self.store.sell_book("test", 6)
        self.assertEqual("test has not enough copies to sell. Left: 5", str(s.exception))

        self.assertEqual("Sold 2 copies of test", self.store.sell_book("test", 2))
        self.assertEqual("Sold 2 copies of test", self.store.sell_book("test", 2))
        self.assertEqual({"test": 1}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(4, self.store.total_sold_books)

    def test__str__(self):
        self.assertEqual("Total sold books: 0\nCurrent availability: 0", self.store.__str__())
        self.store.receive_book("test", 5)
        self.store.receive_book("test2", 5)
        self.store.sell_book("test", 3)
        self.store.sell_book("test2", 2)
        self.assertEqual("Total sold books: 5\nCurrent availability: 5\n - test: 2 copies\n - test2: 3 copies",
                         self.store.__str__())


if __name__ == "__main__":
    main()
