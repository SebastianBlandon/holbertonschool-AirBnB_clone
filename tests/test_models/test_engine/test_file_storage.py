#!/usr/bin/python3
""" Testing File Storage """
import unittest
import os
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User


class Test_FileStorage(unittest.TestCase):
    """ Class for Testing the class FileStorage """
    def setUp(self):
        self.storage = FileStorage()
        test_args = {'updated_at': datetime(2017, 2, 12, 00, 31, 53, 331997),
                     'id': 'f519fb40-1f5c-458b-945c-2ee8eaaf4900',
                     'created_at': datetime(2017, 2, 12, 00, 31, 53, 331900)}
        self.model = BaseModel(test_args)

        self.test_len = 1
        if os.path.isfile("file.json"):
            self.test_len = len(self.storage.all())

    def tearDown(self):
        if os.path.isfile("file.json"):
            os.remove('file.json')

    def test_all(self):
        self.assertEqual(len(self.storage.all()), self.test_len)

    def test_new(self):
        """Testing the 'new' method"""

        Model = BaseModel()

        models.storage.new(Model)
        dict = models.storage.all()

        key_inside = f"{type(Model).__name__}.{Model.id}"
        all_keys = dict.keys()
        self.assertIn(key_inside, all_keys)
        self.assertEqual(dict[key_inside], Model)

    def test_save(self):
        """Testing the 'save' method"""

        Model = BaseModel()

        Model.save()
        self.assertTrue(exists("file.json"))
        with open("file.json") as file:
            to_load = json.load(file)
        self.assertTrue(Model.to_dict() in to_load.values())

    def test_reload(self):
        """Testing the 'reload' method"""

        Model = BaseModel()
        Model_2 = FileStorage()

        Model_2.save()
        Model_2.reload()
        key = f"BaseModel.{Model.id}"
        dict_all = Model_2.all()
        self.assertFalse(dict_all[key] is Model)


if __name__ == "__main__":
    unittest.main()
