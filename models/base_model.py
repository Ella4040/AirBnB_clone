#!/usr/bin/python3
"""
This is definition of the BaseModel class
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    This is a class that defines all common attributes/methods
    for other classes.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialization...
        """
        from models import storage
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"] :
                    self.created_at = datetime.datetime.\
                                      strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    self.updated_at = datetime.datetime.\
                                      strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    continue
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self) #New element  
    
    def save(self):
        """Update the instance's public attribute with today's date
        """
        self.updated_at = datetime.now()
        models.storage.save()
    
    def __str__(self):
        """
        To print
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__
        )
    
    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        """
        class_name = self.__class__.__name__
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = class_name
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
