#!/usr/bin/python3
""" TEST_CASES for BaseModel class
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittests for BaseModel class."""

    def setUp(self):
        """Setting Instantiation"""
        self.base_model = BaseModel()

    def test_id_generation(self):
        """Testing Unique ID generation method
        """
        self.assertIsNotNone(self.base_model.id)

    def test_created_at(self):
        """Testing the 'craeted_at' attribute assingment
        """
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at(self):
        """Testing the 'updated_at' attribute assingment
        """
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_attributes_assignment(self):
        """Testing Atrribute assignment
        """
        attributes = {
            "name": "Test",
            "value": 10,
            "created_at": "2023-07-15T12:00:00.000000",
            "updated_at": "2023-07-15T12:30:00.000000",
        }
        base_model = BaseModel(**attributes)
        self.assertEqual(base_model.name, "Test")
        self.assertEqual(base_model.value, 10)
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_to_dict(self):
        """Teing to_dict() method
        """
        base_model_dict = self.base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)
        self.assertIn("__class__", base_model_dict)
        self.assertIn("created_at", base_model_dict)
        self.assertIn("updated_at", base_model_dict)

    def test_save(self):
        initial_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(initial_updated_at, self.base_model.updated_at)

    def test_str(self):
        base_model_str = str(self.base_model)
        self.assertIsInstance(base_model_str, str)
        self.assertIn("[BaseModel]", base_model_str)
        self.assertIn(self.base_model.id, base_model_str)
        self.assertIn(str(self.base_model.__dict__), base_model_str)

class TestBaseModel(unittest.TestCase):

    def test_save(self):
        bm = BaseModel()
        time_before_save = datetime.utcnow()
        bm.save()
        self.assertTrue(bm.updated_at > time_before_save)

if __name__ == "__main__":
    unittest.main()
