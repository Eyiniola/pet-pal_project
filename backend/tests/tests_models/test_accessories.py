#!/usr/bin/python3

import unittest
from unittest.mock import patch, MagicMock
from models.accesories import Accessories, ShoppingCart

class TestAccessories(unittest.TestCase):
    @patch('models.accesories.db')
    def test_accessories(self, mock_db):
        accessories = Accessories()
        self.assertEqual(accessories.__repr__(), "<Accessories(id=None, name=None)>")

class TestShoppingCart(unittest.TestCase):
    @patch('models.accesories.db')
    def test_shopping_cart(self, mock_db):
        shopping_cart = ShoppingCart(id=1, name='shopping_cart', pet_id=1, user_id=1, item_id=1, quantity=1, price=1)
        self.assertEqual(shopping_cart.__repr__(), "<ShoppingCart(id=1, name=shopping_cart)>")

if __name__ == '__main__':
    unittest.main()
