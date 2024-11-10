from project.furniture import Furniture
from unittest import TestCase, main


class TestFurniture(TestCase):

    def setUp(self) -> None:
        self.furniture = Furniture("Test model", 300.00, (250, 120, 50))

    def test_init(self):
        self.assertIsInstance(self.furniture.model, str)
        self.assertIsInstance(self.furniture.price, float)
        self.assertIsInstance(self.furniture.dimensions, tuple)
        self.assertEqual(True, self.furniture.in_stock)

    def test_model(self):
        self.assertEqual("Test model", self.furniture.model)
        with self.assertRaises(ValueError) as f:
            self.furniture.model = ''
        self.assertEqual("Model must be a non-empty string with a maximum length of 50 characters.", str(f.exception))
        with self.assertRaises(ValueError) as f:
            self.furniture.model = 'This is test model with over fifty characters that raise value error'
        self.assertEqual("Model must be a non-empty string with a maximum length of 50 characters.", str(f.exception))

    def test_price(self):
        self.assertEqual(300.00, self.furniture.price)
        with self.assertRaises(ValueError) as f:
            self.furniture.price = -1.0
        self.assertEqual("Price must be a non-negative number.", str(f.exception))

    def test_dimension(self):
        self.assertEqual((250, 120, 50), self.furniture.dimensions)

        with self.assertRaises(ValueError) as f:
            self.furniture.dimensions = (250, 120)
        self.assertEqual("Dimensions tuple must contain 3 integers.", str(f.exception))

        with self.assertRaises(ValueError) as f:
            self.furniture.dimensions = (250, 120, 0)
        self.assertEqual("Dimensions tuple must contain integers greater than zero.", str(f.exception))

    def test_weight(self):
        self.assertEqual(None, self.furniture.weight)
        self.furniture.weight = 1.5
        self.assertEqual(1.5, self.furniture.weight)
        with self.assertRaises(ValueError) as f:
            self.furniture.weight -= 1.5
        self.assertEqual("Weight must be greater than zero.", str(f.exception))

    def test_get_available_status(self):
        self.assertEqual(f"Model: Test model is currently in stock.", self.furniture.get_available_status())
        self.furniture.in_stock = False
        self.assertEqual(f"Model: Test model is currently unavailable.", self.furniture.get_available_status())

    def test_get_specifications(self):
        self.assertEqual("Model: Test model has the following dimensions: 250mm x 120mm x 50mm and weighs: N/A",
                         self.furniture.get_specifications())
        self.furniture.weight = 5
        self.assertEqual("Model: Test model has the following dimensions: 250mm x 120mm x 50mm and weighs: 5",
                         self.furniture.get_specifications())


if __name__ == "__main__":
    main()