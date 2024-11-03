from project import Mammal
from unittest import TestCase, main


class TestMammal(TestCase):

    def setUp(self) -> None:
        self.dog = Mammal("Kara", "Pomeranian", "bark")

    def test_init(self):
        self.assertEqual("Kara", self.dog.name)
        self.assertEqual("Pomeranian", self.dog.type)
        self.assertEqual("bark", self.dog.sound)

    def test_make_sound(self):
        self.assertEqual("Kara makes bark", self.dog.make_sound())

    def test_get_kingdom(self):
        self.assertEqual("animals", self.dog.get_kingdom())

    def test_info(self):
        self.assertEqual("Kara is of type Pomeranian", self.dog.info())


if __name__ == "__main__":
    main()
