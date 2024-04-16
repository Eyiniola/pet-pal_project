#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from services.database import db


class Accessories(db.Base):
    __tablename__ = 'accessories'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    price = Column(Integer)
    image = Column(String(100))

    def __repr__(self):
        return "<Accessories(id={self.id}, name={self.name})>"
    
class AccessoryShoppingCart(db.Base):
    __tablename__ = 'accessory_shopping_cart'

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
