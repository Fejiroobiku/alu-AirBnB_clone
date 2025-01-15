#!/usr/bin/python
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a place."""
    name = ""
    place_id = ""
    user_id = ""
    text = ""
