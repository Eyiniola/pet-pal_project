#!/usr/bin/python3

from sqlalchemy.orm import sessionmaker
from models.medical import DoctorAppointment, CheckAppointment, Immunization
from models.adopt import Pets, Users
from services.database import db

class MedicalService:
    def __init__(self):
        self.session = db.Session()

    def get_doctor_appointments(self):
        return self.session.query(DoctorAppointment).all()
    
    def get_doctor_appointment(self, appointment_id):
        return self.session.query(DoctorAppointment).filter(DoctorAppointment.id == appointment_id).first()
    
    def get_check_appointments(self):
        return self.session.query(CheckAppointment).all()
    
    def get_check_appointment(self, appointment_id):
        return self.session.query(CheckAppointment).filter(CheckAppointment.id == appointment_id).first()
    
    def get_immunizations(self):
        return self.session.query(Immunization).all()
    
    def get_immunization(self, immunization_id):
        return self.session.query(Immunization).filter(Immunization.id == immunization_id).first()
    
    def add_doctor_appointment(self, pet_id, user_id, date, time, purpose):
        user = self.session.query(Users).filter(Users.id == user_id).first()
        pet = self.session.query(Pets).filter(Pets.id == pet_id).first()
        appointment = DoctorAppointment(pet_id=pet_id, user_id=user_id, date=date, time=time, purpose=purpose)
        self.session.add(appointment)
        self.session.commit()
        return appointment
    
    def update_doctor_appointment(self, appointment_id, date, time, purpose):
        appointment = self.session.query(DoctorAppointment).filter(DoctorAppointment.id == appointment_id).first()
        appointment.date = date
        appointment.time = time
        appointment.purpose = purpose
        self.session.commit()
        return appointment
    
MedicalServices = MedicalService()