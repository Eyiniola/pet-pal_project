#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from services.database import db

# Base = declarative_base()

class Pets(db.Base):
    __tablename__ = 'pets'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    gender = Column(String(10))
    breed = Column(String(50))
    description = Column(String(500))
    image = Column(String(100))

    def __repr__(self):
        return "<Pets(id={self.id}, name={self.name})>"

class AdoptionShoppingCart(db.Base):
    __tablename__ = 'adoption_shopping_cart'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    pet_id = Column(Integer, ForeignKey('pets.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    item_id = Column(Integer)
    quantity = Column(Integer)
    price = Column(Integer)
    pet = relationship('Pets', back_populates='shopping_cart')
    user = relationship('Users', back_populates='shopping_cart')

    def __repr__(self):
        return "<ShoppingCart(id={self.id}, name={self.name})>"
    
class Users(db.Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(50))
    password = Column(String(50))
    shopping_cart = relationship('ShoppingCart', back_populates='user')

    def __repr__(self):
        return "<Users(id={self.id}, name={self.name})>"
    
