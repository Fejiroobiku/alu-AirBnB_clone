#!/usr/bin/python3
import uuid
import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        """Constructor to initialize BaseModel instance."""
        if kwargs:
            self.id = kwargs['id']
            self.created_at = datetime.datetime.fromisoformat(
                kwargs['created_at'])
            self.updated_at = datetime.datetime.fromisoformat(
                kwargs['updated_at'])
        else:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns a string representation of the object."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Saves the object to JSON file."""
        from models import storage
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the object"""
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = str(self.__class__.__name__)
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy
