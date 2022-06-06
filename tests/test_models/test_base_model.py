#!/usr/bin/python3
"""Defines unittests for models/base_model.py

    Unittest classes:
        TestBaseModel_instantiation
        TestBaseModel_save
        TestBaseModel_to_dict
"""
import unittest
from time import sleep
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for testing the instantiation of the BaseModel class."""

    def test_no_args_instantiation(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_exists(self):
        self.assertTrue(BaseModel().id)

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_id_is_unique(self):
        self.assertNotEqual(BaseModel().id, BaseModel().id)

    def test_created_at_exists(self):
        self.assertTrue(BaseModel().created_at)

    def test_created_at_is_public_datetime(self):
        self.assertTrue(type(BaseModel().created_at), datetime)

    def test_two_models_different_created_at(self):
        model1 = BaseModel()
        sleep(0.05)
        model2 = BaseModel()
        self.assertLess(model1.created_at, model2.created_at)

    def test_created_at_does_not_change(self):
        model = BaseModel()
        sleep(0.05)
        created_at = model.created_at
        model.save()
        self.assertEqual(model.created_at, created_at)

    def test_updated_at_exists(self):
        self.assertTrue(BaseModel().updated_at)

    def test_updated_at_is_public_datetime(self):
        self.assertTrue(type(BaseModel().updated_at), datetime)

    def test_updated_at_updates(self):
        model = BaseModel()
        updated_at = model.updated_at
        sleep(0.05)
        model.save()
        self.assertNotEqual(updated_at, model.updated_at)


class TestBaseModel_save(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

    def test_save_exits(self):
        self.assertIn("save", dir(BaseModel()))

    def test_save_updates_updated_at_attr(self):
        model = BaseModel()
        updated_at = model.updated_at
        sleep(0.05)
        model.save()
        self.assertNotEqual(updated_at, model.updated_at)

    def test_save_with_arg(self):
        model = BaseModel()
        with self.assertRaises(TypeError):
            model.save(datetime.utcnow())


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittest for testing to_dict method of the BaseModel class."""

    def test_to_dict_exits(self):
        self.assertTrue(BaseModel().to_dict())

    def test_to_dict_type(self):
        model = BaseModel()
        self.assertTrue(type(model.to_dict()), dict)

    def test_to_dict_contains_correct_keys(self):
        model = BaseModel()
        self.assertIn("id", model.to_dict())
        self.assertIn("created_at", model.to_dict())
        self.assertIn("updated_at", model.to_dict())
        self.assertIn("__class__", model.to_dict())

    def test_to_dict_contains_added_keys(self):
        model = BaseModel()
        model.name = "Ubuntu"
        model.version = 22.04
        self.assertIn("name", model.to_dict())
        self.assertIn("version", model.to_dict())


if __name__ == "__main__":
    unittest.main()
