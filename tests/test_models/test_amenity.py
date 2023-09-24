#!/usr/bin/python3
""" TEST_CASES for Amenity class
"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test for Amenity class"""

    def setUp(self):
        """Setting Instantiation"""
        self.amenity = Amenity()

    def test_default_attr(self):
        """Testing Default attributes"""
        self.assertEqual(self.amenity.name, "")

    def test_update_attr(self):
        """ "Testing updating of attributes"""
        self.amenity.name = "Ikoyi"

        self.assertEqual(self.amenity.name, "Ikoyi")

    def test_inheritance(self):
        """Testing the inheritance of the class Amenity"""
        self.assertIsInstance(self.amenity, Amenity)
        self.assertIsInstance(self.amenity, BaseModel)
