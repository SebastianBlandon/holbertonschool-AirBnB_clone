import unittest
from datetime import datetime
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
    """
    Test the base model class
    """

    def setUp(self):
        self.model1 = BaseModel()

        test_args = {'created_at': datetime(2017, 2, 10, 2, 6, 55, 258849),
                     'updated_at': datetime(2017, 2, 10, 2, 6, 55, 258966),
                     'id': '46458416-e5d5-4985-aa48-a2b369d03d2a',
                     'name': 'model1'}
        self.model2 = BaseModel(test_args)
        self.model2.save()

    def test_instantiation(self):
        self.assertIsInstance(self.model1, BaseModel)
        self.assertTrue(hasattr(self.model1, "created_at"))
        self.assertTrue(hasattr(self.model1, "id"))
        self.assertTrue(hasattr(self.model1, "updated_at"))

    def test_to_dict(self):
        dicti = self.model2.to_dict()
        self.assertNotEqual(self.model2.__dict__, dicti)
        self.assertNotIsInstance(dicti["created_at"], datetime)
        self.assertNotIsInstance(dicti["updated_at"], datetime)
        self.assertTrue(hasattr(dicti, "__class__"))
        self.assertEqual(dicti["__class__"], "BaseModel")

    def test_save(self):
        """Testing the 'save' method"""

        Model = BaseModel()

        Model.save()
        self.assertTrue(exists("file.json"))
        with open("file.json") as file:
            to_load = json.load(file)
        self.assertTrue(Model.to_dict() in to_load.values())


if __name__ == "__main__":
    unittest.main()
