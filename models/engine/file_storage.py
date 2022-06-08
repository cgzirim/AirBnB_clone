#!/usr/bin/python3
"""Defines a class FileStorage"""
import json
from os.path import exists
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file
    to instances.
    """

    def __init__(self):
        """Initialize the FileStorage class."""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        dictionary = {}
        for key, obj in self.__objects.items():
            dictionary[key] = obj.to_dict()
        with open(self.__file_path, "w") as json_file:
            json.dump(dictionary, json_file, ensure_ascii=False)

    def reload(self):
        """Deserializes JSON file to __objects. Does nothing if the JSON file
        doesn't exist.
        """
        if exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as json_file:
                for key, value in json.load(json_file).items():
                    obj = eval(value["__class__"])(**value)
                    self.__objects[key] = obj
