#!/usr/bin/python3
""" City Module for HBNB project """
from lib2to3.pytree import Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey, String
from models.base_model import BaseModel


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey(state_id), nullable=False)
