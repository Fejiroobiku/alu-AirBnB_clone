import uuid
from datetime import datetime
from models.engine.file_storage import FileStorage

class BaseModel:

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.
        If kwargs is provided, loads attributes from dictionary representation.
        Otherwise, creates a new instance with a unique ID and timestamps.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the `updated_at` attribute and saves the instance to storage.
        """
        self.updated_at = datetime.now()  # Update the `updated_at` field
        storage = FileStorage()  # FileStorage manages saving objects
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.
        """
        dict_representation = self.__dict__.copy()
        dict_representation["created_at"] = self.created_at.isoformat()
        dict_representation["updated_at"] = self.updated_at.isoformat()
        dict_representation["__class__"] = self.__class__.__name__
        return dict_representation
