from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class TestShoppingCart(TestCase):

    def setUp(self) -> None:
        self.cart = ShoppingCart("Test", 25.00)

    def test_init_(self):
        self.assertEqual("Test", self.cart.shop_name)
        self.assertEqual(25.00, self.cart.budget)
        self.assertEqual({}, self.cart.products)

    def test_shop_name(self):

        with self.assertRaises(ValueError) as c:
            self.cart.shop_name = "test"
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(c.exception))

        with self.assertRaises(ValueError) as c:
            self.cart.shop_name = "Test1"
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(c.exception))

        self.cart.shop_name = "TEst"
        self.assertEqual("TEst", self.cart.shop_name)

    def test_add_to_cart(self):
        with self.assertRaises(ValueError) as c:
            self.cart.add_to_cart("abc", 100.0)
        self.assertEqual(f"Product abc cost too much!", str(c.exception))
        self.assertEqual({}, self.cart.products)

        self.assertEqual("abc product was successfully added to the cart!", self.cart.add_to_cart("abc", 99.9))
        self.assertEqual({"abc": 99.9}, self.cart.products)

    def test_remove_from_cart(self):
        self.cart.add_to_cart("abc", 10.0)
        self.cart.add_to_cart("aaa", 20.0)

        with self.assertRaises(ValueError) as c:
            self.cart.remove_from_cart("Abc")
        self.assertEqual("No product with name Abc in the cart!", str(c.exception))
        self.assertEqual({"abc": 10.0, "aaa": 20.0}, self.cart.products)

        self.assertEqual("Product abc was successfully removed from the cart!", self.cart.remove_from_cart("abc"))
        self.assertEqual({"aaa": 20.0}, self.cart.products)

    def test_add_(self):
        self.cart.add_to_cart("abc", 10.0)

        new_cart = ShoppingCart("Shop", 100.0)
        self.cart.add_to_cart("Abc", 10.5)

        result = self.cart.__add__(new_cart)
        self.assertEqual(result.shop_name, "TestShop")
        self.assertEqual(result.budget, 125.0)
        self.assertEqual(result.products, {"abc": 10.0, "Abc": 10.5})

    def test_buy_products(self):
        self.cart.add_to_cart("abc", 5.0)
        self.cart.add_to_cart("Abc", 10.0)
        self.assertEqual(f'Products were successfully bought! Total cost: 15.00lv.', self.cart.buy_products())

        with self.assertRaises(ValueError) as c:
            self.cart.add_to_cart("ddd", 10.1)
            self.cart.buy_products()
        self.assertEqual("Not enough money to buy the products! Over budget with 0.10lv!", str(c.exception))


if __name__ == "__main__":
    main()