#!/usr/bin/python3
""" Tests for Place class """

import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """ Testing Method """

    def test_instances_of_User(self):
        """ Testing instances User """

        Model = Place()

        self.assertTrue(hasattr(Model, "city_id"))
        self.assertTrue(hasattr(Model, "user_id"))
        self.assertTrue(hasattr(Model, "name"))
        self.assertTrue(hasattr(Model, "description"))
        self.assertTrue(hasattr(Model, "number_rooms"))
        self.assertTrue(hasattr(Model, "number_bathrooms"))
        self.assertTrue(hasattr(Model, "max_guest"))
        self.assertTrue(hasattr(Model, "price_by_night"))
        self.assertTrue(hasattr(Model, "latitude"))
        self.assertTrue(hasattr(Model, "longitude"))
        self.assertTrue(hasattr(Model, "amendity_ids"))

    def test_type_objects_User(self):
        """ Testing type onjects User """

        Model = User()

        self.assertIsInstance(Model.city_id, str)
        self.assertIsInstance(Model.user_id, str)
        self.assertIsInstance(Model.name, str)
        self.assertIsInstance(Model.description, str)
        self.assertIsInstance(Model.number_rooms, int)
        self.assertIsInstance(Model.number_bathrooms, int)
        self.assertIsInstance(Model.max_guest, int)
        self.assertIsInstance(Model.price_by_night, int)
        self.assertIsInstance(Model.latitude, float)
        self.assertIsInstance(Model.longitude, float)
        self.assertIsInstance(Model.amendity_ids, list)

        self.assertTrue(issubclass(Place, BaseModel))


if __name__ == '__main__':
    unittest.main()
