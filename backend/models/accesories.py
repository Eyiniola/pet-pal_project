#!/usr/bin/python3

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class accesory(Base):
    __tablename__ = 'accesory'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    description = Column(String)
    image = Column(String)

    def __repr__(self):
        return "<accesory(id={self.id}, name={self.name}, type={self.type}, description={self.description}, image={self.image})>"
    