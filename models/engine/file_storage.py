#!/usr/bin/python3
import json
import sys
sys.path.append('..')


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns all the objects present at the moment."""
        return self.__objects

    def new(self, obj):
        """Keeps a new object into a class attribute."""
        self.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        """Saves all the objects into a JSON file."""
        serialized_data = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(serialized_data, f)

    def reload(self):
        """Loads back objects saved into a JSON file."""
        from models.base_model import BaseModel
        from models.review import Review
        from models.place import Place
        from models.amenity import Amenity
        from models.city import City
        from models.state import State
        from models.user import User

        try:
            with open(self.__file_path, 'r') as f:
                retrieved_data = json.load(f)
                for k, v in retrieved_data.items():
                    self.new(eval(f"{v['__class__']}")(**v))
        except FileNotFoundError:
            pass
