#!/usr/bin/python3
from models.base_model import BaseModel
import sys
sys.path.append('..')


class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel"""
    name = ""
