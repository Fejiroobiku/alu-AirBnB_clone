#!/usr/bin/python3
"""
Unit test cases for the BaseModel class.
"""

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Unit test cases for the BaseModel class.
    """

    def test_init(self):
        """
        Test initialization of a BaseModel instance.
        """
        my_model = BaseModel()
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_save(self):
        """
        Test that the save method updates the `updated_at` attribute.
        """
        my_model = BaseModel()
        initial_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(initial_updated_at, my_model.updated_at)

    def test_to_dict(self):
        """
        Test the dictionary representation of a BaseModel instance.
        """
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertEqual(my_model_dict["__class__"], 'BaseModel')
        self.assertEqual(my_model_dict['id'], my_model.id)
        self.assertEqual(my_model_dict['created_at'], my_model.created_at.isoformat())
        self.assertEqual(my_model_dict['updated_at'], my_model.updated_at.isoformat())

    def test_str(self):
        """
        Test the string representation of a BaseModel instance.
        """
        my_model = BaseModel()
        output = str(my_model)
        self.assertTrue(output.startswith("[BaseModel]"))
        self.assertIn(my_model.id, output)

if __name__ == '__main__':
    unittest.main()
