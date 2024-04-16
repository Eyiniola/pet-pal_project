#!/usr/bin/python3

import unittest
from unittest.mock import patch
from models.adopt import Pets, ShoppingCart, Users


class TestPets(unittest.TestCase):
    @patch('models.adopt.db')
    def test_pets(self, mock_db):
        pets = Pets()
        self.assertEqual(pets.__repr__(), "<Pets(id=None, name=None)>")

class TestShoppingCart(unittest.TestCase):
    @patch('models.adopt.db')
    def test_shopping_cart(self, mock_db):
        shopping_cart = ShoppingCart(id=1, name='shopping_cart', pet_id=1, user_id=1, item_id=1, quantity=1, price=1)
        self.assertEqual(shopping_cart.__repr__(), "<ShoppingCart(id=1, name=shopping_cart)>")

class TestUsers(unittest.TestCase):
    @patch('models.adopt.db')
    def test_users(self, mock_db):
        users = Users()
        self.assertEqual(users.__repr__(), "<Users(id=None, name=None)>")


if __name__ == '__main__':
    unittest.main()