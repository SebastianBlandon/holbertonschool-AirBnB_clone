#!/usr/bin/python3
""" Tests for User class """

import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """ Testing Method """

    def test_instances_of_User(self):
        """ Testing instances User """

        Model = User()

        self.assertTrue(hasattr(Model, "email"))
        self.assertTrue(hasattr(Model, "password"))
        self.assertTrue(hasattr(Model, "first_name"))
        self.assertTrue(hasattr(Model, "last_name"))

    def test_type_objects_User(self):
        """ Testing type onjects User """

        Model = User()

        self.assertIsInstance(Model.email, str)
        self.assertIsInstance(Model.password, str)
        self.assertIsInstance(Model.first_name, str)
        self.assertIsInstance(Model.last_name, str)

        self.assertTrue(issubclass(User, BaseModel))


if __name__ == '__main__':
    unittest.main()
