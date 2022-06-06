#!/usr/bin/python3
"""Defines a class BaseModel"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes."""

    def __init__(self):
        """Initialize the BaseModel class."""
        self.id = uuid4()
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __str__(self):
        """Returns string representation of model."""
        d = self.__dict__

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, d)

    def save(self):
        """Updates the instance attribute `updated_at` with current datetime"""
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of
        the instance.
        """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = datetime.isoformat(self.created_at)
        dictionary["updated_at"] = datetime.isoformat(self.updated_at)
        return dictionary
