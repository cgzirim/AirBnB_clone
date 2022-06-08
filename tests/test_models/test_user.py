#!/usr/bin/python3
"""Defines unittests for models/user.py

Unittest classes:
        TestUser_instantiation
        TestUser__str__
        TestUser_save
        TestUser_to_dict
"""
import unittest
from models.user import User
from time import sleep
from datetime import datetime


class TestUser_instantiation(unittest.TestCase):
    """Unittests for the instantiation of the User class."""

    def test_no_args_instantiation(self):
        self.assertEqual(User, type(User()))

    def test_id_exists(self):
        self.assertTrue(User().id)

    def test_id_is_public_str(self):
        self.assertEqual(str, type(User().id))

    def test_id_is_unique(self):
        self.assertNotEqual(User().id, User().id)

    def test_created_at_exists(self):
        self.assertTrue(User().created_at)

    def test_created_at_is_public_datetime(self):
        self.assertTrue(type(User().created_at), datetime)

    def test_two_models_different_created_at(self):
        model1 = User()
        sleep(0.05)
        model2 = User()
        self.assertLess(model1.created_at, model2.created_at)

    def test_created_at_does_not_change(self):
        model = User()
        sleep(0.05)
        created_at = model.created_at
        model.save()
        self.assertEqual(model.created_at, created_at)

    def test_updated_at_exists(self):
        self.assertTrue(User().updated_at)

    def test_updated_at_is_public_datetime(self):
        self.assertTrue(type(User().updated_at), datetime)

    def test_updated_at_updates(self):
        model = User()
        updated_at = model.updated_at
        sleep(0.05)
        model.save()
        self.assertNotEqual(updated_at, model.updated_at)

    def test_email_is_public_str(self):
        self.assertEqual(str, type(User().email))

    def test_password_is_public_str(self):
        self.assertEqual(str, type(User().password))

    def test_first_name_is_public_str(self):
        self.assertEqual(str, type(User().first_name))

    def test_last_name_is_public_str(self):
        self.assertEqual(str, type(User().last_name))


class TestUser__str__(unittest.TestCase):
    """Unittest for testing __str__ method of the User class."""

    def test_str_exists(self):
        self.assertIn("__str__", dir(User()))

    def test_str_type(self):
        model = User()
        self.assertEqual(type(model.__str__()), str)

    def test_arg_in_str(self):
        model = User()
        with self.assertRaises(TypeError):
            model.__str__(None)

    def test_str_representation(self):
        dt = datetime.utcnow()
        dt_repr = repr(dt)
        model = User()
        model.id = "12345"
        model.created_at = model.updated_at = dt
        modelstr = model.__str__()
        self.assertIn("[User] (12345)", modelstr)
        self.assertIn("'id': '12345'", modelstr)
        self.assertIn("'created_at': " + dt_repr, modelstr)
        self.assertIn("'updated_at': " + dt_repr, modelstr)


class TestUser_save(unittest.TestCase):
    """Unittests for testing save method of the User class."""

    def test_save_exists(self):
        self.assertIn("save", dir(User()))

    def test_save_updates_updated_at_attr(self):
        model = User()
        updated_at = model.updated_at
        sleep(0.05)
        model.save()
        self.assertNotEqual(updated_at, model.updated_at)

    def test_save_calls_storage(self):
        model = User()
        model.save()
        with open("file.json", "r") as f:
            key = "User." + model.id
            self.assertIn(key, f.read())

    def test_save_with_arg(self):
        model = User()
        with self.assertRaises(TypeError):
            model.save(datetime.utcnow())


class TestUser_to_dict(unittest.TestCase):
    """Unittest for testing to_dict method of the User class."""

    def test_to_dict_exits(self):
        self.assertTrue(User().to_dict())

    def test_to_dict_type(self):
        model = User()
        self.assertTrue(type(model.to_dict()), dict)

    def test_to_dict_contains_correct_keys(self):
        model = User()
        model.email = "holberton@example.com"
        model.password = "HoLbErToN"
        model.first_name = "Holberton"
        model.last_name = "Betty"
        self.assertIn("id", model.to_dict())
        self.assertIn("created_at", model.to_dict())
        self.assertIn("updated_at", model.to_dict())
        self.assertIn("email", model.to_dict())
        self.assertIn("password", model.to_dict())
        self.assertIn("first_name", model.to_dict())
        self.assertIn("last_name", model.to_dict())

    def test_to_dict_contains_added_keys(self):
        model = User()
        model.name = "Ubuntu"
        model.version = 22.04
        self.assertIn("name", model.to_dict())
        self.assertIn("version", model.to_dict())


if __name__ == "__main__":
    unittest.main()
