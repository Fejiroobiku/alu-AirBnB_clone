#!/usr/bin/python3
"""test for the FileStorage class"""

import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage(unittest.TestCase):
    def test_all(self):
        self.assertIsInstance(models.storage.all(), dict)

    def test_new(self):
        obj = State()
        all_objects = models.storage.all()
        self.assertIn("State.{}".format(obj.id), all_objects)

    def test_save(self):
        obj = City()
        models.storage.new(obj)
        models.storage.save()
        with open('file.json', 'r') as file:
            data = json.load(file)
            self.assertIn("City.{}".format(obj.id), data)

    def test_reload(self):
        obj = City()
        models.storage.new(obj)
        models.storage.save()
        models.storage.reload()
        objs = models.storage.all()
        self.assertIn("City.{}".format(obj.id), objs)


if __name__ == '__main__':
    unittest.main()    
