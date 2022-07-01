#!/usr/bin/python3
"""
    class BaseModel that defines all common attributes/methods for other classes
"""
from uuid import uuid4
from datetime import datetime


class BaseModel():
    """ class BaseModel """
    def __init__(self):
        """ Method __init__ initialize the all attibutes """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        return "[{}] ({}) {}"\
                .format(BaseModel.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.today()

    def to_dict(self):
        self.created_at = str(self.created_at.isoformat("T"))
        self.updated_at = str(self.updated_at.isoformat("T"))
        return self.__dict__

