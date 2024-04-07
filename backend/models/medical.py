#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from ..services.database import db

class DoctorAppointment(db.Base):
    __tablename__ = 'doctor_appointment'

    id = Column(Integer, primary_key=True)
    pet_id = Column(Integer, ForeignKey('pets.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    date = Column(Date)
    time = Column(String(10))
    purpose = Column(String(255))

    user = relationship('Users', backref='doctor_appointment')
    pet = relationship('Pets', backref='doctor_appointment')
   
    def __repr__(self):
        return "<DoctorAppointment(id={self.id}, pet_id={self.pet_id}, user_id={user_id})>"
    
class CheckAppointment(db.Base):
    __tablename__ = 'check_appointment'

    id = Column(Integer, primary_key=True)
    pet_id = Column(Integer, ForeignKey('pets.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    date = Column(Date)
    time = Column(String(10))
    purpose = Column(String(255))

    user = relationship('Users', backref='check_appointment')
    pet = relationship('Pets', backref='check_appointment')
   
    def __repr__(self):
        return "<CheckAppointment(id={self.id}, pet_id={self.pet_id}, user_id={user_id})>"
    
class Immunization(db.Base):
    __tablename__ = 'immunization'

    id = Column(Integer, primary_key=True)
    pet_id = Column(Integer, ForeignKey('pets.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    date = Column(Date)
    time = Column(String(10))
    purpose = Column(String(255))

    user = relationship('Users', backref='immunization')
    pet = relationship('Pets', backref='immunization')
   
    def __repr__(self):
        return "<Immunization(id={self.id}, pet_id={self.pet_id}, user_id={user_id})>"
    
