#!/usr/bin/python3

from sqlalchemy.orm import sessionmaker
from models.accesories import Accessories, ShoppingCart
from services.database import db

class AdoptService:
    def __init__(self):
        self.session = db.Session()

    def get_all_toys(self):
        return self.session.query(Accessories).all()
    
    def get_shopping_cart(self):
        return self.session.query(ShoppingCart).all()
    
    def get_cart_item(self, item_id):
        return self.session.query(ShoppingCart).filter(ShoppingCart.item_id == item_id).first()
    
    def add_to_cart(self, user_id, item_id, quantity, price):
        item = self.session.query(Accessories).filter(Accessories.id == item_id).first()
        cart_item = ShoppingCart(name=item.name, item_id=item_id, user_id=user_id, quantity=quantity, price=price)
        self.session.add(cart_item)
        self.session.commit()
        return cart_item
    
    def remove_from_cart(self, item_id):
        cart_item = self.session.query(ShoppingCart).filter(ShoppingCart.item_id == item_id).first()
        self.session.delete(cart_item)
        self.session.commit()
        return cart_item
    
    def update_cart(self, item_id, quantity):
        cart_item = self.session.query(ShoppingCart).filter(ShoppingCart.item_id == item_id).first()
        cart_item.quantity = quantity
        self.session.commit()
        return cart_item
    
    def checkout(self, user_id):
        cart_items = self.session.query(ShoppingCart).filter(ShoppingCart.user_id == user_id).all()
        for cart_item in cart_items:
            self.session.delete(cart_item)
        self.session.commit()
        return cart_items
    
AdoptServices = AdoptService()