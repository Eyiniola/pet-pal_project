#!/usr/bin/python3

from flask import request, jsonify, Blueprint
from ..services.medical_services import MedicalServices


medical = Blueprint('medical', __name__, url_prefix='/medical')

@medical.route('/appointments', methods=['GET'])
def get_doctor_appointments():
    appointments = MedicalServices.get_doctor_appointments()
    return jsonify([appointment.__dict__ for appointment in appointments])

@medical.route('/appointments/<int:appointment_id>', methods=['GET'])
def get_doctor_appointment(appointment_id):
    appointment = MedicalServices.get_doctor_appointment(appointment_id)
    return jsonify(appointment.__dict__)

@medical.route('/checkups', methods=['GET'])
def get_check_appointments():
    appointments = MedicalServices.get_check_appointments()
    return jsonify([appointment.__dict__ for appointment in appointments])

@medical.route('/checkups/<int:appointment_id>', methods=['GET'])
def get_check_appointment(appointment_id):
    appointment = MedicalServices.get_check_appointment(appointment_id)
    return jsonify(appointment.__dict__)

@medical.route('/immunizations', methods=['GET'])
def get_immunizations():
    immunizations = MedicalServices.get_immunizations()
    return jsonify([immunization.__dict__ for immunization in immunizations])

@medical.route('/immunizations/<int:immunization_id>', methods=['GET'])
def get_immunization(immunization_id):
    immunization = MedicalServices.get_immunization(immunization_id)
    return jsonify(immunization.__dict__)

@medical.route('/appointments/add', methods=['POST'])
def add_doctor_appointment():
    pet_id = request.json['pet_id']
    user_id = request.json['user_id']
    date = request.json['date']
    time = request.json['time']
    purpose = request.json['purpose']
    appointment = MedicalServices.add_doctor_appointment(pet_id, user_id, date, time, purpose)
    return jsonify(appointment.__dict__)

@medical.route('/appointments/update', methods=['PUT'])
def update_doctor_appointment():
    appointment_id = request.json['appointment_id']
    date = request.json['date']
    time = request.json['time']
    purpose = request.json['purpose']
    appointment = MedicalServices.update_doctor_appointment(appointment_id, date, time, purpose)
    return jsonify(appointment.__dict__)

