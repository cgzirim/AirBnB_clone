#!/usr/bin/python3
"""Defines unittests for models/Amenity.py

Unittest classes:
        TestAmenity_instantiation
        TestAmenity__str__
        TestAmenity_save
        TestAmenity_to_dict
"""
import unittest
from models.amenity import Amenity
from time import sleep
from datetime import datetime


class TestAmenity_instantiation(unittest.TestCase):
    """Unittests for the instantiation of the Amenity class."""

    def test_no_args_instantiation(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_id_exists(self):
        self.assertTrue(Amenity().id)

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_id_is_unique(self):
        self.assertNotEqual(Amenity().id, Amenity().id)

    def test_created_at_exists(self):
        self.assertTrue(Amenity().created_at)

    def test_created_at_is_public_datetime(self):
        self.assertTrue(type(Amenity().created_at), datetime)

    def test_two_models_different_created_at(self):
        model1 = Amenity()
        sleep(0.05)
        model2 = Amenity()
        self.assertLess(model1.created_at, model2.created_at)

    def test_created_at_does_not_change(self):
        model = Amenity()
        sleep(0.05)
        created_at = model.created_at
        model.save()
        self.assertEqual(model.created_at, created_at)

    def test_updated_at_exists(self):
        self.assertTrue(Amenity().updated_at)

    def test_updated_at_is_public_datetime(self):
        self.assertTrue(type(Amenity().updated_at), datetime)

    def test_updated_at_updates(self):
        model = Amenity()
        updated_at = model.updated_at
        sleep(0.05)
        model.save()
        self.assertNotEqual(updated_at, model.updated_at)

    def test_name_is_public_str(self):
        self.assertEqual(str, type(Amenity().name))


class TestAmenity__str__(unittest.TestCase):
    """Unittest for testing __str__ method of the Amenity class."""

    def test_str_exists(self):
        self.assertIn("__str__", dir(Amenity()))

    def test_str_type(self):
        model = Amenity()
        self.assertEqual(type(model.__str__()), str)

    def test_arg_in_str(self):
        model = Amenity()
        with self.assertRaises(TypeError):
            model.__str__(None)

    def test_str_representation(self):
        dt = datetime.utcnow()
        dt_repr = repr(dt)
        model = Amenity()
        model.id = "12345"
        model.created_at = model.updated_at = dt
        modelstr = model.__str__()
        self.assertIn("[Amenity] (12345)", modelstr)
        self.assertIn("'id': '12345'", modelstr)
        self.assertIn("'created_at': " + dt_repr, modelstr)
        self.assertIn("'updated_at': " + dt_repr, modelstr)


class TestAmenity_save(unittest.TestCase):
    """Unittests for testing save method of the Amenity class."""

    def test_save_exists(self):
        self.assertIn("save", dir(Amenity()))

    def test_save_updates_updated_at_attr(self):
        model = Amenity()
        updated_at = model.updated_at
        sleep(0.05)
        model.save()
        self.assertNotEqual(updated_at, model.updated_at)

    def test_save_calls_storage(self):
        model = Amenity()
        model.save()
        with open("file.json", "r") as f:
            key = "Amenity." + model.id
            self.assertIn(key, f.read())

    def test_save_with_arg(self):
        model = Amenity()
        with self.assertRaises(TypeError):
            model.save(datetime.utcnow())


class TestAmenity_to_dict(unittest.TestCase):
    """Unittest for testing to_dict method of the Amenity class."""

    def test_to_dict_exits(self):
        self.assertTrue(Amenity().to_dict())

    def test_to_dict_type(self):
        model = Amenity()
        self.assertTrue(type(model.to_dict()), dict)

    def test_to_dict_contains_correct_keys(self):
        model = Amenity()
        model.name = "WiFi"
        self.assertIn("id", model.to_dict())
        self.assertIn("created_at", model.to_dict())
        self.assertIn("updated_at", model.to_dict())
        self.assertIn("name", model.to_dict())

    def test_to_dict_contains_added_keys(self):
        model = Amenity()
        model.name = "Ubuntu"
        model.version = 22.04
        self.assertIn("name", model.to_dict())
        self.assertIn("version", model.to_dict())


if __name__ == "__main__":
    unittest.main()
