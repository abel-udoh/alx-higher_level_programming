#!/usr/bin/python3
"""A file that contains the class definition of a State and an instance
   Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import State, Base


class City(Base):
    """
        inherits from Base (imported from model_state)
        links to the MySQL table cities
    """
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
