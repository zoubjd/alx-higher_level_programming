#!/usr/bin/python3
""" Define City model """
from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import Base, State


class City(Base):
    """ Define a class City to be linked to db table """
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False,
                autoincrement=True, unique=True,
                primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
