#!/usr/bin/python3
"""User module for the HBNB project"""
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

# Determine storage type
storage_type = getenv("HBNB_TYPE_STORAGE")


class User(BaseModel, Base):
    """User class for representing users"""
    
    __tablename__ = 'users' if storage_type == 'db' else None

    email = Column(String(128), nullable=False) if storage_type == 'db' else ""
    password = Column(String(128), nullable=False) if storage_type == 'db' else ""
    first_name = Column(String(128), nullable=True) if storage_type == 'db' else ""
    last_name = Column(String(128), nullable=True) if storage_type == 'db' else ""

    if storage_type == 'db':
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")

    def __init__(self, *args, **kwargs):
        """Initializes a User instance"""
        super().__init__(*args, **kwargs)