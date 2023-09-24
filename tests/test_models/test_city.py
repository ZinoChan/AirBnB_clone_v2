#!/usr/bin/python3
""" TEST_CASES for City class
"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """ Unittest for City Class
    """
    def setUp(self):
        """Setting Instantiation"""
        self.city = City()

    def test_default_attr(self):
        """testing default attributes
        """
        self.assertEqual(self.city.name, "")
        self.assertEqual(self.city.state_id, "")

    def test_update_attr(self):
        """Testing updating of attributes"""
        self.city.name = "Tokyo"
        self.city.state_id = "Shinjuku"

        self.assertEqual(self.city.name, "Tokyo")
        self.assertEqual(self.city.state_id, "Shinjuku")

    def test_inheritance(self):
        """Testing the inheritance of the class Review"""
        self.assertIsInstance(self.city, City)
        self.assertIsInstance(self.city, BaseModel)


if __name__ == "__main__":
    unittest.main()
