#!/usr/bin/python3
from models.base_model import BaseModel
import sys
sys.path.append('..')


class City(BaseModel):
    """City class that inherits from BaseModel."""
    state_id = ""
    name = ""
