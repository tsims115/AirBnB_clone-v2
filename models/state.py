#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
            'City', cascade="all, delete, delete-orphan", backref="state")
    else:
        @property
        def cities(self):
            """Cities getter for FileStorage"""
            from models import storage
            city_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """returns cities for current state"""
            from models import storage

            cities = []
            for k, v in storage.all(City).items():
                if self.id == v.__dict__['state_id']:
                    cities.append(v)
            return cities
