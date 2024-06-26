#!/usr/bin/python3

from sqlalchemy.orm import sessionmaker
from models.adopt import Pets, AdoptionShoppingCart, Users
from services.database import db

class AdoptService:
    def __init__(self):
        self.session = db.Session()

    def create_pet(self, data):
        name = data.get('name')
        age = data.get('age')
        breed = data.get('breed')
        price = data.get('price')
        image = data.get('image')

        if name is None or age is None or breed is None or price is None or image is None:
            return None
        pet = Pets(name=name, age=age, breed=breed, price=price, image=image)
        self.session.add(pet)
        self.session.commit()
        return pet

    def get_pets(self):
        return self.session.query(Pets).all()
    
    def get_pet(self, pet_id):
        return self.session.query(Pets).filter(Pets.id == pet_id).first()
    
    def get_shopping_cart(self):
        return self.session.query(AdoptionShoppingCart).all()
    
    def get_user(self, user_id):
        return self.session.query(Users).filter(Users.id == user_id).first()
    
    def add_to_cart(self, user_id, pet_id, quantity, price):
        user = self.get_user(user_id)
        pet = self.get_pet(pet_id)
        item_id = len(self.get_shopping_cart()) + 1
        cart_item = AdoptionShoppingCart(name=pet.name, pet_id=pet_id, user_id=user_id, item_id=item_id, quantity=quantity, price=price)
        self.session.add(cart_item)
        self.session.commit()
        return cart_item
    
    def remove_from_cart(self, item_id):
        cart_item = self.session.query(AdoptionShoppingCart).filter(AdoptionShoppingCart.item_id == item_id).first()
        self.session.delete(cart_item)
        self.session.commit()
        return cart_item
    
    def update_cart(self, item_id, quantity):
        cart_item = self.session.query(AdoptionShoppingCart).filter(AdoptionShoppingCart.item_id == item_id).first()
        cart_item.quantity = quantity
        self.session.commit()
        return cart_item
    
    def checkout(self, user_id):
        user = self.get_user(user_id)
        cart_items = self.session.query(AdoptionShoppingCart).filter(AdoptionShoppingCart.user_id == user_id).all()
        for cart_item in cart_items:
            self.session.delete(cart_item)
        self.session.commit()
        return cart_items
    
AdoptServices = AdoptService()

