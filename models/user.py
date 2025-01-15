#!/usr/bin/python3
"""User model class"""
from models.base_model import BaseModel


class User(BaseModel):
    """A class for the User model"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initialize the data model"""
        super().__init__(*args, **kwargs)
