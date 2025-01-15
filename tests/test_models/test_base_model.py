#!/usr/bin/python3
"""Script to test the BaseModel class using unittest."""
import os
import json
from uuid import UUID
import datetime
import unittest
from models.base_model import BaseModel
import sys
sys.path.append('C:\\Users\\mbric\\Documents\\Sook\\alu-AirBnB_clone')


class TestBaseModel(unittest.TestCase):
    """Class which will be used to test BaseModel class. """

    def __init__(self, *args, **kwargs):
        """Sets up basic attributes."""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ """
        obj = self.value()
        self.assertEqual(type(obj), self.value)

    def test_kwargs(self):
        """ """
        obj = self.value()
        copy = obj.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is obj)

    def test_save(self):
        """ Testing save """
        obj = self.value()
        obj.save()
        key = self.name + "." + obj.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], obj.to_dict())

    def test_str(self):
        obj = self.value()
        self.assertEqual(str(obj), '[{}] ({}) {}'.format(self.name, obj.id,
                         obj.__dict__))

    def test_to_dict(self):
        created_at = datetime.datetime(2024, 5, 10, 12, 0, 0).isoformat()
        updated_at = datetime.datetime(2024, 5, 10, 13, 0, 0).isoformat()
        obj = BaseModel(id='test_id', created_at=created_at,
                        updated_at=updated_at)
        expected_dict = {'id': 'test_id', 'created_at': '2024-05-10T12:00:00',
                         'updated_at': '2024-05-10T13:00:00', '__class__': 'BaseModel'}
        self.assertEqual(obj.to_dict(), expected_dict)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)


if __name__ == '__main__':
    unittest.main()
