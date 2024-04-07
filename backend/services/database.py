#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Database:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)
        self.Base = Base

db = Database('mysql://petPalAdmin:petPalAdmin1244@localhost/pet_pal_project')
