#!/usr/bin/python3
"""Defines unittests for models/state.py

Unittest classes:
        TestState_instantiation
        TestState__str__
        TestState_save
        TestState_to_dict
"""
import unittest
from models.state import State
from time import sleep
from datetime import datetime


class TestState_instantiation(unittest.TestCase):
    """Unittests for the instantiation of the State class."""

    def test_no_args_instantiation(self):
        self.assertEqual(State, type(State()))

    def test_id_exists(self):
        self.assertTrue(State().id)

    def test_id_is_public_str(self):
        self.assertEqual(str, type(State().id))

    def test_id_is_unique(self):
        self.assertNotEqual(State().id, State().id)

    def test_created_at_exists(self):
        self.assertTrue(State().created_at)

    def test_created_at_is_public_datetime(self):
        self.assertTrue(type(State().created_at), datetime)

    def test_two_models_different_created_at(self):
        model1 = State()
        sleep(0.05)
        model2 = State()
        self.assertLess(model1.created_at, model2.created_at)

    def test_created_at_does_not_change(self):
        model = State()
        sleep(0.05)
        created_at = model.created_at
        model.save()
        self.assertEqual(model.created_at, created_at)

    def test_updated_at_exists(self):
        self.assertTrue(State().updated_at)

    def test_updated_at_is_public_datetime(self):
        self.assertTrue(type(State().updated_at), datetime)

    def test_updated_at_updates(self):
        model = State()
        updated_at = model.updated_at
        sleep(0.05)
        model.save()
        self.assertNotEqual(updated_at, model.updated_at)

    def test_name_is_public_str(self):
        self.assertEqual(str, type(State().name))


class TestState__str__(unittest.TestCase):
    """Unittest for testing __str__ method of the State class."""

    def test_str_exists(self):
        self.assertIn("__str__", dir(State()))

    def test_str_type(self):
        model = State()
        self.assertEqual(type(model.__str__()), str)

    def test_arg_in_str(self):
        model = State()
        with self.assertRaises(TypeError):
            model.__str__(None)

    def test_str_representation(self):
        dt = datetime.utcnow()
        dt_repr = repr(dt)
        model = State()
        model.id = "12345"
        model.created_at = model.updated_at = dt
        modelstr = model.__str__()
        self.assertIn("[State] (12345)", modelstr)
        self.assertIn("'id': '12345'", modelstr)
        self.assertIn("'created_at': " + dt_repr, modelstr)
        self.assertIn("'updated_at': " + dt_repr, modelstr)


class TestState_save(unittest.TestCase):
    """Unittests for testing save method of the State class."""

    def test_save_exists(self):
        self.assertIn("save", dir(State()))

    def test_save_updates_updated_at_attr(self):
        model = State()
        updated_at = model.updated_at
        sleep(0.05)
        model.save()
        self.assertNotEqual(updated_at, model.updated_at)

    def test_save_calls_storage(self):
        model = State()
        model.save()
        with open("file.json", "r") as f:
            key = "State." + model.id
            self.assertIn(key, f.read())

    def test_save_with_arg(self):
        model = State()
        with self.assertRaises(TypeError):
            model.save(datetime.utcnow())


class TestState_to_dict(unittest.TestCase):
    """Unittest for testing to_dict method of the State class."""

    def test_to_dict_exits(self):
        self.assertTrue(State().to_dict())

    def test_to_dict_type(self):
        model = State()
        self.assertTrue(type(model.to_dict()), dict)

    def test_to_dict_contains_correct_keys(self):
        model = State()
        model.name = "Betty"
        self.assertIn("id", model.to_dict())
        self.assertIn("created_at", model.to_dict())
        self.assertIn("updated_at", model.to_dict())
        self.assertIn("name", model.to_dict())

    def test_to_dict_contains_added_keys(self):
        model = State()
        model.name = "Ubuntu"
        model.version = 22.04
        self.assertIn("name", model.to_dict())
        self.assertIn("version", model.to_dict())


if __name__ == "__main__":
    unittest.main()
