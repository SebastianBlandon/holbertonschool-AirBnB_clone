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
        self.model.save()
        self.assertEqual(len(self.storage.all()), self.test_len + 1)
        a = BaseModel()
        a.save()
        self.assertEqual(len(self.storage.all()), self.test_len + 2)

    def test_save(self):
        self.test_len = len(self.storage.all())
        a = BaseModel()
        a.save()
        self.assertEqual(len(self.storage.all()), self.test_len + 1)
        b = User()
        self.assertEqual(len(self.storage.all()), self.test_len + 2)
        b.save()
        self.assertEqual(len(self.storage.all()), self.test_len + 2)

    def test_reload(self):
        pass

if __name__ == "__main__":
    unittest.main()
