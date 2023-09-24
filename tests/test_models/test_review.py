#!/usr/bin/python3
""" TEST_CASES for Review class
"""
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    def setUp(self):
        """Setting Instantiation"""
        self.review = Review()

    def test_default_attr(self):
        """Testing for default attributes"""
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.text, "")

    def test_update_attr(self):
        """Testing updating of attributes"""
        self.review.user_id = "MikEL6535"
        self.review.place_id = "Lagos33996"
        self.review.text = "i love lagos, it is a beautiful place to stay"

        self.assertEqual(self.review.user_id, "MikEL6535")
        self.assertEqual(self.review.place_id, "Lagos33996")
        self.assertEqual(
            self.review.text, "i love lagos, it is a beautiful place to stay"
        )

    def test_inheritance(self):
        """Testing the inheritance of the class Review"""
        self.assertIsInstance(self.review, Review)
        self.assertIsInstance(self.review, BaseModel)
