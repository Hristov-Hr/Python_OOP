from Python_OOP.testing_lab.list import IntegerList

import unittest


class IntegerListTest(unittest.TestCase):

    def setUp(self):
        self.i = IntegerList(1, 1.15, "asd", 8, (2, 8))

    def test_init(self):
        self.assertEqual([1, 8], self.i.get_data())

    def test_add(self):
        self.assertEqual([1, 8, 12], self.i.add(12))
        with self.assertRaises(ValueError) as e:
            self.i.add("ddd")
        self.assertEqual("Element is not Integer", str(e.exception))

    def test_remove_index(self):
        self.assertEqual(8, self.i.remove_index(1))
        self.assertEqual([1], self.i.get_data())
        self.assertEqual(1, self.i.remove_index(0))
        self.assertEqual([], self.i.get_data())
        with self.assertRaises(IndexError) as e:
            self.i.remove_index(2)
        self.assertEqual("Index is out of range", str(e.exception))

    def test_get(self):
        self.assertEqual(1, self.i.get(0))
        self.assertEqual(8, self.i.get(1))
        with self.assertRaises(IndexError) as e:
            self.i.get(2)
        self.assertEqual("Index is out of range", str(e.exception))

    def test_insert(self):
        with self.assertRaises(ValueError) as e:
            self.i.insert(1, "ddd")
        self.assertEqual("Element is not Integer", str(e.exception))

        with self.assertRaises(IndexError) as e:
            self.i.insert(2, 5)
        self.assertEqual("Index is out of range", str(e.exception))

        self.i.insert(1, 12)
        self.assertEqual([1, 12, 8], self.i.get_data())

    def test_get_biggest(self):
        self.assertEqual(8, self.i.get_biggest())

    def test_get_index(self):
        self.assertEqual(1, self.i.get_index(8))


if __name__ == "__main__":
    unittest.main()