#!/usr/bin/python3
"""Defines unittests for models/city.py

Unittest classes:
        TestCity_instantiation
        TestCity__str__
        TestCity_save
        TestCity_to_dict
"""
import unittest
from models.city import City
from time import sleep
from datetime import datetime


class TestCity_instantiation(unittest.TestCase):
    """Unittests for the instantiation of the City class."""

    def test_no_args_instantiation(self):
        self.assertEqual(City, type(City()))

    def test_id_exists(self):
        self.assertTrue(City().id)

    def test_id_is_public_str(self):
        self.assertEqual(str, type(City().id))

    def test_id_is_unique(self):
        self.assertNotEqual(City().id, City().id) 

    def test_created_at_exists(self):
        self.assertTrue(City().created_at)

    def test_created_at_is_public_datetime(self):
        self.assertTrue(type(City().created_at), datetime)

    def test_two_models_different_created_at(self):
        model1 = City()
        sleep(0.05)
        model2 = City()
        self.assertLess(model1.created_at, model2.created_at)

    def test_created_at_does_not_change(self):
        model = City()
        sleep(0.05)
        created_at = model.created_at
        model.save()
        self.assertEqual(model.created_at, created_at)

    def test_updated_at_exists(self):
        self.assertTrue(City().updated_at)

    def test_updated_at_is_public_datetime(self):
        self.assertTrue(type(City().updated_at), datetime)

    def test_updated_at_updates(self):
        model = City()
        updated_at = model.updated_at
        sleep(0.05)
        model.save()
        self.assertNotEqual(updated_at, model.updated_at)

    def test_state_id_is_public_str(self):
        self.assertEqual(str, type(City().state_id))

    def test_name_public_str(self):
        self.assertEqual(str, type(City().name))    


class TestCity__str__(unittest.TestCase):
    """Unittest for testing __str__ method of the City class."""

    def test_str_exists(self):
        self.assertIn("__str__", dir(City()))

    def test_str_type(self):
        model = City()
        self.assertEqual(type(model.__str__()), str)

    def test_arg_in_str(self):
        model = City()
        with self.assertRaises(TypeError):
            model.__str__(None)

    def test_str_representation(self):
        dt = datetime.utcnow()
        dt_repr = repr(dt)
        model = City()
        model.id = "12345"
        model.created_at = model.updated_at = dt
        modelstr = model.__str__()
        self.assertIn("[City] (12345)", modelstr)
        self.assertIn("'id': '12345'", modelstr)
        self.assertIn("'created_at': " + dt_repr, modelstr)
        self.assertIn("'updated_at': " + dt_repr, modelstr)


class TestCity_save(unittest.TestCase):
    """Unittests for testing save method of the City class."""

    def test_save_exists(self):
        self.assertIn("save", dir(City()))

    def test_save_updates_updated_at_attr(self):
        model = City()
        updated_at = model.updated_at
        sleep(0.05)
        model.save()
        self.assertNotEqual(updated_at, model.updated_at)

    def test_save_calls_storage(self):
        model = City()
        model.save()
        with open("file.json", "r") as f:
            key = "City." + model.id
            self.assertIn(key, f.read())

    def test_save_with_arg(self):
        model = City()
        with self.assertRaises(TypeError):
            model.save(datetime.utcnow())


class TestCity_to_dict(unittest.TestCase):
    """Unittest for testing to_dict method of the City class."""

    def test_to_dict_exits(self):
        self.assertTrue(City().to_dict())

    def test_to_dict_type(self):
        model = City()
        self.assertTrue(type(model.to_dict()), dict)

    def test_to_dict_contains_correct_keys(self):
        model = City()
        model.name = "Lagos"
        model.state_id = "1234-1234-1234"
        self.assertIn("id", model.to_dict())
        self.assertIn("created_at", model.to_dict())
        self.assertIn("updated_at", model.to_dict())
        self.assertIn("name", model.to_dict())
        self.assertIn("state_id", model.to_dict())
        
    def test_to_dict_contains_added_keys(self):
        model = City()
        model.name = "Ubuntu"
        model.version = 22.04
        self.assertIn("name", model.to_dict())
        self.assertIn("version", model.to_dict())


if __name__ == "__main__":
    unittest.main()