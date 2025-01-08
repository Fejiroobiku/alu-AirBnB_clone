#!/usr/bin/python3
"""
This module defines the BaseModel class, which serves as the base for all future classes in the project.
"""

from datetime import datetime
import models
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid

# Define a format for datetime string representation
TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

# Set up SQLAlchemy's Base class for models using a database
if models.storage_t == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """BaseModel class defines common attributes and methods for other models."""
    
    if models.storage_t == "db":
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
        updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        """Initializes an instance of BaseModel with the provided keyword arguments."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at

        # Assign attributes from kwargs
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" and isinstance(value, str):
                    self.created_at = datetime.strptime(value, TIME_FORMAT)
                elif key == "updated_at" and isinstance(value, str):
                    self.updated_at = datetime.strptime(value, TIME_FORMAT)
                elif key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the 'updated_at' attribute and saves the instance to storage."""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Converts the instance to a dictionary, with proper formatting."""
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.strftime(TIME_FORMAT)
        new_dict["updated_at"] = self.updated_at.strftime(TIME_FORMAT)
        new_dict["__class__"] = self.__class__.__name__

        # Remove SQLAlchemy state from dictionary (if present)
        new_dict.pop("_sa_instance_state", None)
        return new_dict

    def delete(self):
        """Deletes the current instance from storage."""
        models.storage.delete(self)	