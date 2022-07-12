#!/usr/bin/python3
""" Tests for Amenity class """

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ Testing Method """

    def test_instances_of_State(self):
        """ Testing instances Amenity """

        Model = Amenity()

        self.assertTrue(hasattr(Model, "name"))

    def test_type_objects_State(self):
        """ Testing type onjects Amenity """

        Model = Amenity()

        self.assertIsInstance(Model, Amenity)

        self.assertIsInstance(Model.name, str)

        self.assertTrue(issubclass(Amenity, BaseModel))


if __name__ == '__main__':
    unittest.main()
