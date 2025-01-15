#!/usr/bin/python3

import json
from models.base_model import BaseModel

class FileStorage:
    """
    Class to serialize instances to a JSON file and
    deserialize JSON file to instances.
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Returns the dictionary of all stored objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the storage dictionary with key `<class name>.id`.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes the __objects dictionary to a JSON file.
        """
        data = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        """
        Deserializes the JSON file back into __objects, if the file exists.
        """
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, obj_dict in data.items():
                    class_name = obj_dict["__class__"]
                    self.__objects[key] = eval(class_name)(**obj_dict)
        except FileNotFoundError:
            pass
