#!/usr/bin/python3
""" containd the Base class for AirBnB console
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Class BaseModel"""
    def __init__(self, *args, **kwargs):
        """ initialize new instance of BaseModel with a unique id"""
        self.id = str(uuid4())
        dtform = "%Y-%m-%dT%H:%M:%S.%f"
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == "created_at" or j == "updated_at":
                    self.__dict__[i] = datetime.strptime(j, dtform)
                else:
                    self.__dict__[i] = j

    def __str__(self):
        nm = self.__class__.__name__
        return "[{}] ({}) {}".format(nm, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
