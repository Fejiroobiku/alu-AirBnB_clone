#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from os import getenv

# Retrieve the storage type from the environment
storage_type = getenv("HBNB_TYPE_STORAGE")


class Review(BaseModel, Base):
    """ Review class to store review information """
    __tablename__ = "reviews" if storage_type == 'db' else None

    place_id = Column(String(60), ForeignKey("places.id"), nullable=False) if storage_type == 'db' else ""
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False) if storage_type == 'db' else ""
    text = Column(String(1024), nullable=False) if storage_type == 'db' else ""

    def __init__(self, *args, **kwargs):
        """Initializes the Review object"""
        super().__init__(*args, **kwargs)