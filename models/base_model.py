#!/usr/bin/python3
"""
    class BaseModel that defines all common attributes/methods for other classes
"""
from uuid import uuid4
from datetime import date


class BaseModel():
    """ class BaseModel """
    def __init__(self):
        """ Method __init__ initialize the all attibutes """
        self.id = str(uuid4())
        self.created_at = date.today()
        self.updated_at = date.today()

    def __str__(self):
        return "[{}] ({}) {}"\
                .format(self.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = date.today()

    def to_dict(self):
        return self.__dict__

