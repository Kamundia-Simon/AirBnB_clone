#!/usr/bin/python3
"""Defines unittests for models/base_model.py.

Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """Unittests for the BaseModel class."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_instance_creation(self):
        """Test instantiation of BaseModel."""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)

    def test_id_generation(self):
        """Test if unique id is generated."""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_created_at_type(self):
        """Test if created_at attribute is datetime type."""
        my_model = BaseModel()
        self.assertIsInstance(my_model.created_at, datetime)

    def test_updated_at_type(self):
        """Test if updated_at attribute is datetime type."""
        my_model = BaseModel()
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_str_representation(self):
        """Test the __str__ representation."""
        my_model = BaseModel()
        str_repr = str(my_model)
        self.assertIn("[BaseModel]", str_repr)
        self.assertIn(str(my_model.id), str_repr)
        self.assertIn(str(my_model.__dict__), str_repr)

    def test_save_method(self):
        """Test the save method."""
        my_model = BaseModel()
        original_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(original_updated_at, my_model.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method."""
        my_mod = BaseModel()
        my_mod.name = "Test Mod"
        my_mod.my_number = 42
        my_mod_dict = my_mod.to_dict()

        self.assertEqual(my_mod_dict['id'], my_mod.id)
        self.assertEqual(my_mod_dict['__class__'], 'BaseModel')
        self.assertEqual(my_mod_dict['created_at'],
                         my_mod.created_at.isoformat())
        self.assertEqual(my_mod_dict['updated_at'],
                         my_mod.updated_at.isoformat())
        self.assertEqual(my_mod_dict['name'], "Test Mod")
        self.assertEqual(my_mod_dict['my_number'], 42)

    def test_save_updates_file(self):
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        all_objects = models.storage.all()
        self.assertIn(bmid, all_objects)

        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())

    def test_save_with_storage_new(self):
        bm = BaseModel()
        original_updated_at = bm.updated_at
        bm.save()
        stored_model = models.storage.all().get(bm.id)
        self.assertIsNotNone(stored_model)
        self.assertEqual(original_updated_at, stored_model.updated_at)


if __name__ == "__main__":
    unititest.main()
