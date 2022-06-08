#!/usr/bin/python3
"""Defines unittests for models/review.py

Unittest classes:
        TestReview_instantiation
        TestReview__str__
        TestReview_save
        TestReview_to_dict
"""
import unittest
from models.review import Review
from time import sleep
from datetime import datetime


class TestReview_instantiation(unittest.TestCase):
    """Unittests for the instantiation of the Review class."""

    def test_no_args_instantiation(self):
        self.assertEqual(Review, type(Review()))

    def test_id_exists(self):
        self.assertTrue(Review().id)

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Review().id))

    def test_id_is_unique(self):
        self.assertNotEqual(Review().id, Review().id) 

    def test_created_at_exists(self):
        self.assertTrue(Review().created_at)

    def test_created_at_is_public_datetime(self):
        self.assertTrue(type(Review().created_at), datetime)

    def test_two_models_different_created_at(self):
        model1 = Review()
        sleep(0.05)
        model2 = Review()
        self.assertLess(model1.created_at, model2.created_at)

    def test_created_at_does_not_change(self):
        model = Review()
        sleep(0.05)
        created_at = model.created_at
        model.save()
        self.assertEqual(model.created_at, created_at)

    def test_updated_at_exists(self):
        self.assertTrue(Review().updated_at)

    def test_updated_at_is_public_datetime(self):
        self.assertTrue(type(Review().updated_at), datetime)

    def test_updated_at_updates(self):
        model = Review()
        updated_at = model.updated_at
        sleep(0.05)
        model.save()
        self.assertNotEqual(updated_at, model.updated_at)

    def test_place_id_is_public_str(self):
        self.assertEqual(str, type(Review().place_id))

    def test_user_id_is_public_str(self):
        self.assertEqual(str, type(Review().user_id))

    def test_text_is_public_str(self):
        self.assertEqual(str, type(Review().text))

class TestReview__str__(unittest.TestCase):
    """Unittest for testing __str__ method of the Review class."""

    def test_str_exists(self):
        self.assertIn("__str__", dir(Review()))

    def test_str_type(self):
        model = Review()
        self.assertEqual(type(model.__str__()), str)

    def test_arg_in_str(self):
        model = Review()
        with self.assertRaises(TypeError):
            model.__str__(None)

    def test_str_representation(self):
        dt = datetime.utcnow()
        dt_repr = repr(dt)
        model = Review()
        model.id = "12345"
        model.created_at = model.updated_at = dt
        modelstr = model.__str__()
        self.assertIn("[Review] (12345)", modelstr)
        self.assertIn("'id': '12345'", modelstr)
        self.assertIn("'created_at': " + dt_repr, modelstr)
        self.assertIn("'updated_at': " + dt_repr, modelstr)


class TestReview_save(unittest.TestCase):
    """Unittests for testing save method of the Review class."""

    def test_save_exists(self):
        self.assertIn("save", dir(Review()))

    def test_save_updates_updated_at_attr(self):
        model = Review()
        updated_at = model.updated_at
        sleep(0.05)
        model.save()
        self.assertNotEqual(updated_at, model.updated_at)

    def test_save_calls_storage(self):
        model = Review()
        model.save()
        with open("file.json", "r") as f:
            key = "Review." + model.id
            self.assertIn(key, f.read())

    def test_save_with_arg(self):
        model = Review()
        with self.assertRaises(TypeError):
            model.save(datetime.utcnow())


class TestReview_to_dict(unittest.TestCase):
    """Unittest for testing to_dict method of the Review class."""

    def test_to_dict_exits(self):
        self.assertTrue(Review().to_dict())

    def test_to_dict_type(self):
        model = Review()
        self.assertTrue(type(model.to_dict()), dict)

    def test_to_dict_contains_correct_keys(self):
        model = Review()
        model.place_id = "1234-1234-1234"
        model.user_id = "4321-4321-4321"
        model.text = "I love this place"
        self.assertIn("id", model.to_dict())
        self.assertIn("created_at", model.to_dict())
        self.assertIn("updated_at", model.to_dict())
        self.assertIn("place_id", model.to_dict())
        self.assertIn("user_id", model.to_dict())
        self.assertIn("text", model.to_dict())

    def test_to_dict_contains_added_keys(self):
        model = Review()
        model.name = "Ubuntu"
        model.version = 22.04
        self.assertIn("name", model.to_dict())
        self.assertIn("version", model.to_dict())


if __name__ == "__main__":
    unittest.main()