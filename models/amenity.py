#!/usr/bin/python3
""" Amenity Module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv

# Determine the storage type from the environment
storage_type = getenv("HBNB_TYPE_STORAGE")


class Amenity(BaseModel, Base):
    """ Amenity class representing amenities for places """
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)

    # Optionally define place_amenities relationship if using DB storage
    # place_amenities = relationship("Place", secondary="place_amenity") if storage_type == 'db' else ""