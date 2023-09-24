#!/usr/bin/python3
""" TEST_CASES for User class
"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test for the User class"""

    def setUp(self):
        """Setting Instantiation"""
        self.user = User()

    def test_default_attr(self):
        """Testing for default attributes"""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_update_attr(self):
        """Testing updating of attributes"""
        self.user.email = "sakata@example.com"
        self.user.password = "zuuurrrraaaa"
        self.user.first_name = "Sakata"
        self.user.last_name = "Gintoki"

        self.assertEqual(self.user.email, "sakata@example.com")
        self.assertEqual(self.user.password, "zuuurrrraaaa")
        self.assertEqual(self.user.first_name, "Sakata")
        self.assertEqual(self.user.last_name, "Gintoki")

    def test_inheritance(self):
        """Testing the inheritance of the class Review"""
        self.assertIsInstance(self.user, User)
        self.assertIsInstance(self.user, BaseModel)


if __name__ == "__main__":
    unittest.main()
