#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if len(kwargs) != 0:
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = self.updated_at = datetime.now()
            self._assign_attributes(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        from models import storage

        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dict_rep = self.__dict__.copy()
        dict_rep["__class__"] = self.__class__.__name__
        dict_rep["created_at"] = dict_rep["created_at"].isoformat()
        dict_rep["updated_at"] = dict_rep["updated_at"].isoformat()
        dict_rep.pop("_sa_instance_state", None)
        return dict_rep

    def _assign_attributes(self, attrubutes):
        """Assigns the attrubutes from kwargs"""
        for key, value in attrubutes.items():
            if key != "__class__":
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)

    def delete(self):
        """Delete the current instance from storage"""
        from models import storage

        storage.delete(self)
