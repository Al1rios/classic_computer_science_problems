import unittest
from product import Product
from shopping import ShoppingCart



# class TestShoppingCart(unittest.TestCase):

#     def test_product_object(self):
#         name = "apples"
#         price = 1.70

#         product_one = Product(name, price)


#         self.assertEqual(product_one.name, name)
#         self.assertEqual(product_one.price, 10, 'price is not correct')

# if __name__ == '__main__':
#     unittest.main()

class TestShoppingCart(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print(">>>this method runs once before all tests")

    @classmethod
    def tearDownClass(cls):
        print(">>>this method runs once after all tests")


    def setUp(self) -> None:
        self.name = "Samsung Galaxy S10"
        self.price = 1000
        self.smartphone = Product(self.name, self.price)
        print(">>>this method runs before every test")
        self.shopping_cart_one = ShoppingCart()
        self.shopping_cart_two  = ShoppingCart()
        self.shopping_cart_two.add_product(self.smartphone)
    

    def tearDown(self) -> None:
        pass

    def test_product_object(self):
        pass

    def test_product_name(self):
        self.assertEqual(self.smartphone.name, self.name)

    def test_product_price(self):
        self.assertEqual(self.smartphone.price, self.price)

    def test_empty_shopping_cart(self):
        self.assertTrue(self.shopping_cart_one.is_empty())

    def test_shopping_has_products(self):
        self.assertTrue(self.shopping_cart_two.has_products(self.smartphone))
        self.assertFalse(self.shopping_cart_two.is_empty())
    
        




if __name__ == '__main__':
    unittest.main()