#!/usr/bin/python3
"""
    class FileStorage that serializes instances to a JSON file and deserializes
    JSON file to instances
"""


import json


class FileStorage:
    """serialize instance to json file and deserialize json file to instance"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_obj = {}
        for key in self.__objects:
            json_obj[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w', encoding='UTF-8') as file:
            json.dump(json_obj, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        from models.base_model import BaseModel


        classes = {"BaseModel": BaseModel}

        try:
             with open(self.__file_path, mode="r", encoding="utf-8") as file:
                for key, value in json.load(file).items():
                    self.__objects[key] = classes[value['__class__']](
                        **value)
        except FileNotFoundError:
            pass
