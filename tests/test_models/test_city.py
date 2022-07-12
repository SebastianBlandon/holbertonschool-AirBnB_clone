#!/usr/bin/python3
""" Tests for City class """

import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """ Testing Method """

    def test_instances_of_City(self):
        """ Testing instances City """

        Model = City()

        self.assertTrue(hasattr(Model, "state_id"))
        self.assertTrue(hasattr(Model, "name"))

    def test_type_objects_City(self):
        """ Testing type onjects City """

        Model = City()

        self.assertIsInstance(Model, City)

        self.assertIsInstance(Model.state_id, str)
        self.assertIsInstance(Model.name, str)

        self.assertTrue(issubclass(City, BaseModel))


if __name__ == '__main__':
    unittest.main()
