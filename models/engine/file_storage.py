#!/usr/bin/python3
"""
    class FileStorage that serializes instances to a JSON file and deserializes
    JSON file to instances
"""


import json


class FileStorage:
    """ Class FileStorage """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Method all """
        return self.__objects

    def new(self, obj):
        """ Method new """
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """ Method save """
        json_obj = {}
        for key in self.__objects:
            json_obj[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w', encoding='UTF-8') as file:
            json.dump(json_obj, file)

    def reload(self):
        """ Method reload """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {"BaseModel": BaseModel, "User": User, "Place": Place}
        cls_up = {"State": State, "City": City, "Amenity": Amenity}
        cls_up_ = {"Review": Review}
        classes.update(cls_up)
        classes.update(cls_up_)

        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as f:
                for key, value in json.load(f).items():
                    self.__objects[key] = classes[value['__class__']](**value)
        except FileNotFoundError:
            pass
