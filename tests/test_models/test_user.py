#!/usr/bin/python3
""" Tests for User class """

import unittest

import models
import json
from models.base_model import BaseModel
from models.user import User
from os.path import exists


class TestUser(unittest.TestCase):
    """Testing our functions of 'User'"""

    def test_instances_of_User(self):
        """Testing the 'User' public attributes"""

        Model = User()

        self.assertTrue(hasattr(Model, "email"))
        self.assertTrue(hasattr(Model, "password"))
        self.assertTrue(hasattr(Model, "first_name"))
        self.assertTrue(hasattr(Model, "last_name"))

    def test_type_objects_User(self):
        """Testing type of 'User' attributes (objects)"""

        Model = User()

        self.assertIsInstance(Model.email, str)
        self.assertIsInstance(Model.password, str)
        self.assertIsInstance(Model.first_name, str)
        self.assertIsInstance(Model.last_name, str)

        self.assertTrue(issubclass(User, BaseModel))


if __name__ == '__main__':
    unittest.main()
