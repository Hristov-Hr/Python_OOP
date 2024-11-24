from project.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):

    def setUp(self) -> None:
        self.toy = ToyStore()

    def test_init(self):
        self.assertEqual(self.toy.toy_shelf, {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })

    def test_add_toy(self):

        with self.assertRaises(Exception) as t:
            self.toy.add_toy("I", "test")
        self.assertEqual("Shelf doesn't exist!", str(t.exception))

        self.assertEqual(f"Toy:Test placed successfully!", self.toy.add_toy("A", "Test"))

        with self.assertRaises(Exception) as t:
            self.toy.add_toy("A", "Test2")
        self.assertEqual("Shelf is already taken!", str(t.exception))

        with self.assertRaises(Exception) as t:
            self.toy.add_toy("A", "Test")
        self.assertEqual("Toy is already in shelf!", str(t.exception))

    def test_remove_toy(self):
        with self.assertRaises(Exception) as t:
            self.toy.remove_toy("I", "Test")
        self.assertEqual("Shelf doesn't exist!", str(t.exception))

        self.toy.add_toy("A", "Test")

        with self.assertRaises(Exception) as t:
            self.toy.remove_toy("A", "Test2")
        self.assertEqual("Toy in that shelf doesn't exists!", str(t.exception))

        self.assertEqual(f"Remove toy:Test successfully!", self.toy.remove_toy("A", "Test"))
        self.assertEqual(self.toy.toy_shelf, {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })




if __name__ == "__main__":
    main()