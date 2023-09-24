#!/usr/bin/python3
""" TEST_CASES for Place class
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Unittest for class Place"""

    def setUp(self):
        """Setting Instantiation"""
        self.place = Place()

    def test_default_attr(self):
        """Testing Default attributes"""
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_attr_assignment(self):
        """Testing the inheritance of the class Review"""
        self.place.name = "Tokyo House"
        self.place.city_id = "TOK123"
        self.place.user_id = "USER456"
        self.place.description = "Cozy house in the heart of Tokyo"
        self.place.number_rooms = 2
        self.place.number_bathrooms = 1
        self.place.max_guest = 3
        self.place.price_by_night = 150
        self.place.latitude = 35.6895
        self.place.longitude = 139.6917
        self.place.amenity_ids = ["wifi", "kitchen", "ac"]

        self.assertEqual(self.place.name, "Tokyo House")
        self.assertEqual(self.place.city_id, "TOK123")
        self.assertEqual(self.place.user_id, "USER456")
        self.assertEqual(
            self.place.description, "Cozy house in the heart of Tokyo")
        self.assertEqual(self.place.number_rooms, 2)
        self.assertEqual(self.place.number_bathrooms, 1)
        self.assertEqual(self.place.max_guest, 3)
        self.assertEqual(self.place.price_by_night, 150)
        self.assertEqual(self.place.latitude, 35.6895)
        self.assertEqual(self.place.longitude, 139.6917)
        self.assertEqual(self.place.amenity_ids, ["wifi", "kitchen", "ac"])


if __name__ == "__main__":
    unittest.main()
