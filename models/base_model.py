#!/usr/bin/python3
"""The BaseModel Class"""
from datetime import datetime
from uuid import uuid4
import models
from models.__init__ import storage

class BaseModel:
    def __init__(self, *arg, **kwargs):
        if kwargs:
            for keys, values in kwargs.items():
                if keys != '__class__':
                    setattr(self, keys, values)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """updates the public instance attribute"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        dict_obj = self.__dict__.copy()
        dict_obj['created_at'] = self.created_at.isoformat()
        dict_obj['updated_at'] = self.updated_at.isoformat()
        dict_obj['__class__'] = self.__class__.__name__
        #return {key: dict_obj[key] for key in keys_order}
        return dict_obj

    def __str__(self):
        """print: [<class name>] (<self.id>) <self.__dict__>"""
        return f"[{self.__class__.__name__}]({self.id}) {self.__dict__}"
