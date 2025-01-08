#!/usr/bin/python3
""" City Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

# Determine the storage type from the environment
storage_type = getenv("HBNB_TYPE_STORAGE")


class City(BaseModel, Base):
    """Represents a city in the HBNB project"""
    __tablename__ = 'cities' if storage_type == "db" else None

    state_id = Column(String(60), ForeignKey('states.id'), nullable=False) if storage_type == "db" else ""
    name = Column(String(128), nullable=False) if storage_type == "db" else ""

    # Define relationship if using DB storage
    places = relationship("Place", backref="cities") if storage_type == "db" else None

    def __init__(self, *args, **kwargs):
        """Initializes the city object"""
        super().__init__(*args, **kwargs)