from Python_OOP.testing_lab.test_cat import Cat

from unittest import TestCase, main


class CatTests(TestCase):

    def test_cat_increase_size(self):
        cat = Cat("Tommy")
        cat.eat()
        self.assertEqual(1, cat.size)
        self.assertTrue(cat.fed)

    def test_raise_error(self):

        cat = Cat("Tommy")
        cat.eat()
        with self.assertRaises(Exception) as c:
            cat.eat()
        self.assertEqual('Already fed.', str(c.exception))

        cat = Cat("Tommy")
        with self.assertRaises(Exception) as c:
            cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(c.exception))

        cat = Cat("Tommy")
        cat.eat()
        cat.sleep()
        self.assertFalse(cat.sleepy)


if __name__ == "__main__":
    main()