#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py

    Unittest classes:
        TestFileStorage_initialization
        TestFileStorage_methods
"""
import os
import unittest
import models
from datetime import datetime
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage_initialization(unittest.TestCase):
    """Unittests for the initialization of the FileStorage class."""

    def test_no_args_instantiation(self):
        self.assertEqual(FileStorage, type(FileStorage()))

    def test__file_path_is_private_str(self):
        self.assertEqual(type(FileStorage.__file_path), str)

    def test__objects_is_private_dict(self):
        self.assertEqual(type(FileStorage.__objects), dict)

    def test_with_args_instantiation(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_storage_initialization(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestStorage_methods(unittest.TestCase):
    """Unittests for all methods in the FileStorage class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(type(FileStorage.all()), dict)

    def test_new(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        ct = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(ct)
        models.storage.new(am)
        models.storage.new(rv)
        self.assertIn("{}.{}".format(BaseModel, bm.id), models.storage.all())
        self.assertIn(bm, models.storage.all().values())
        self.assertIn("{}.{}".format(User, us.id), models.storage.all())
        self.assertIn(us, models.storage.all().values())
        self.assertIn("{}.{}".format(State, st.id), models.storage.all())
        self.assertIn(st, models.storage.all().values())
        self.assertIn("{}.{}".format(Place, pl.id), models.storage.all())
        self.assertIn(pl, models.storage.all().values())
        self.assertIn("{}.{}".format(City, ct.id), models.storage.all())
        self.assertIn(ct, models.storage.all().values())
        self.assertIn("{}.{}".format(Amenity, am.id), models.storage.all())
        self.assertIn(am, models.storage.all().values())
        self.assertIn("{}.{}".format(Review, rv.id), models.storage.all())
        self.assertIn(rv, models.storage.all().values())

    def test_with_None(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        ct = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(ct)
        models.storage.new(am)
        models.storage.new(rv)
        models.storage.save()
        with open("file.json", "r") as f:
            content = f.read()
            self.assertIn("BaseModel." + bm.id, content)
            self.assertIn("User." + us.id, content)
            self.assertIn("State." + st.id, content)
            self.assertIn("Place." + pl.id, content)
            self.assertIn("City." + ct.id, content)
            self.assertIn("Amenity." + am.id, content)
            self.assertIn("Review." + rv.id, content)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save()

    def test_reload(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        ct = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(ct)
        models.storage.new(am)
        models.storage.new(rv)
        models.storage.save()
        models.storage.__objects = {}
        models.storage.reload()
        objects = models.storage.__objects
        self.assertIn("BaseModel." + bm.id, objects)
        self.assertIn("User." + us.id, objects)
        self.assertIn("State." + st.id, objects)
        self.assertIn("Place." + pl.id, objects)
        self.assertIn("City." + ct.id, objects)
        self.assertIn("Amenity." + am.id, objects)
        self.assertIn("Review." + rv.id, objects)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload("School")

    def test_reload_no_file(self):
        with self.assertRaises(FileNotFoundError):
            models.storage.reload()
