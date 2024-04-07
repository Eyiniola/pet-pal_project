#!/usr/bin/python3

import unittest
from unittest.mock import patch
from models.medical import DoctorAppointment, CheckAppointment, Immunization


class TestDoctorAppointment(unittest.TestCase):
    @patch('models.medical.db')
    def test_doctor_appointment(self, mock_db):
        doctor_appointment = DoctorAppointment(id=1, pet_id=1, user_id=1, date='2021-01-01', time='12:00', purpose='purpose')
        self.assertEqual(doctor_appointment.__repr__(), "<DoctorAppointment(id=1, pet_id=1, user_id={user_id})>")

class TestCheckAppointment(unittest.TestCase):
    @patch('models.medical.db')
    def test_check_appointment(self, mock_db):
        check_appointment = CheckAppointment(id=1, pet_id=1, user_id=1, date='2021-01-01', time='12:00', purpose='purpose')
        self.assertEqual(check_appointment.__repr__(), "<CheckAppointment(id=1, pet_id=1, user_id={user_id})>")

class TestImmunization(unittest.TestCase):
    @patch('models.medical.db')
    def test_immunization(self, mock_db):
        immunization = Immunization(id=1, pet_id=1, user_id=1, date='2021-01-01', time='12:00', purpose='purpose')
        self.assertEqual(immunization.__repr__(), "<Immunization(id=1, pet_id=1, user_id={user_id})>")


if __name__ == '__main__':
    unittest.main()