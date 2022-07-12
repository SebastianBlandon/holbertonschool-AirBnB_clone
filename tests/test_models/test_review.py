#!/usr/bin/python3
""" Tests for Review class """

import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """ Testing Method """

    def test_instances_of_Review(self):
        """ Testing instances Review """

        Model = Review()

        self.assertTrue(hasattr(Model, "place_id"))
        self.assertTrue(hasattr(Model, "user_id"))
        self.assertTrue(hasattr(Model, "text"))

    def test_type_objects_Review(self):
        """ Testing type onjects User """

        Model = Review()

        self.assertIsInstance(Model.place_id, str)
        self.assertIsInstance(Model.user_id, str)
        self.assertIsInstance(Model.text, str)

        self.assertTrue(issubclass(Review, BaseModel))


if __name__ == '__main__':
    unittest.main()
