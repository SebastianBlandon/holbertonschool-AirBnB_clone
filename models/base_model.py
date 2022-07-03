#!/usr/bin/python3
"""
    class BaseModel that defines all common attributes/methods for other classes
"""
from uuid import uuid4
from datetime import datetime
from models import storage
dateformat = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel():
    """ class BaseModel """
    def __init__(self, *args, **kwargs):
        """ Method __init__ initialize the all attibutes """
        if kwargs:
            for key, val in kwargs.items():
                if key != '__class__':
                    setattr(self, key, val)
                if hasattr(self, 'created_at') and type(self.created_at) is str:
                    self.created_at = datetime.strptime(kwargs["created_at"],\
                            dateformat)
                if hasattr(self, 'updated_at') and type(self.updated_at) is str:
                    self.updated_at = datetime.strptime(kwargs["updated_at"],\
                            dateformat)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            storage.new(self)

    def __str__(self):
        """ __str__ Method """
        return "[{}] ({}) {}"\
                .format(BaseModel.__name__, self.id, self.__dict__)

    def save(self):
        """ save Method """
        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        """ to_dict Method """
        self.__dict__["__class__"] = self.__class__.__name__
        dict_cpy = self.__dict__.copy()
        if "created_at" in self.__dict__:
            dict_cpy["created_at"] = self.created_at.strftime(dateformat)
        if "updated_at" in self.__dict__:
            dict_cpy["updated_at"] = self.updated_at.strftime(dateformat)
        return dict_cpy

