#!/usr/bin/python3
"""Defines unittests for models/place.py.

Unittest classes:
    TestPlace_instantiation
    TestPlace_save
    TestPlace_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_city_id_is_public_str(self):
        self.assertEqual(str, type(Place.city_id))

    def test_user_id_is_public_str(self):
        self.assertEqual(str, type(Place.user_id))

    def test_name_is_public_str(self):
        self.assertEqual(str, type(Place.name))

    def test_description_is_public_str(self):
        self.assertEqual(str, type(Place.description))

    def test_number_rooms_is_public_int(self):
        self.assertEqual(int, type(Place.number_rooms))

    def test_number_bathrooms_is_public_int(self):
        self.assertEqual(int, type(Place.number_bathrooms))

    def test_max_guest_is_public_int(self):
        self.assertEqual(int, type(Place.max_guest))

    def test_price_by_night_is_public_int(self):
        self.assertEqual(int, type(Place.price_by_night))

    def test_latitude_is_public_float(self):
        self.assertEqual(float, type(Place.latitude))

    def test_longitude_is_public_float(self):
        self.assertEqual(float, type(Place.longitude))

    def test_amenity_ids_is_public_list(self):
        self.assertEqual(list, type(Place.amenity_ids))

    def test_two_places_unique_ids(self):
        pl1 = Place()
        pl2 = Place()
        self.assertNotEqual(pl1.id, pl2.id)

    def test_two_places_different_created_at(self):
        pl1 = Place()
        sleep(0.05)
        pl2 = Place()
        self.assertLess(pl1.created_at, pl2.created_at)

    def test_two_places_different_updated_at(self):
        pl1 = Place()
        sleep(0.05)
        pl2 = Place()
        self.assertLess(pl1.updated_at, pl2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        pl = Place()
        pl.id = "123456"
        pl.created_at = pl.updated_at = dt
        plstr = pl.__str__()
        self.assertIn("[Place] (123456)", plstr)
        self.assertIn("'id': '123456'", plstr)
        self.assertIn("'created_at': " + dt_repr, plstr)
        self.assertIn("'updated_at': " + dt_repr, plstr)

    def test_args_unused(self):
        pl = Place(None)
        self.assertNotIn(None, pl.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        pl = Place(
            id="345",
            created_at=dt_iso,
            updated_at=dt_iso,
            city_id="city123",
            user_id="user123",
            name="Example Place",
            description="A beautiful place",
            number_rooms=3,
            number_bathrooms=2,
            max_guest=6,
            price_by_night=100,
            latitude=40.7128,
            longitude=-74.0060,
            amenity_ids=["amenity1", "amenity2"]
        )
        self.assertEqual(pl.id, "345")
        self.assertEqual(pl.created_at, dt)
        self.assertEqual(pl.updated_at, dt)
        self.assertEqual(pl.city_id, "city123")
        self.assertEqual(pl.user_id, "user123")
        self.assertEqual(pl.name, "Example Place")
        self.assertEqual(pl.description, "A beautiful place")
        self.assertEqual(pl.number_rooms, 3)
        self.assertEqual(pl.number_bathrooms, 2)
        self.assertEqual(pl.max_guest, 6)
        self.assertEqual(pl.price_by_night, 100)
        self.assertEqual(pl.latitude, 40.7128)
        self.assertEqual(pl.longitude, -74.0060)
        self.assertEqual(pl.amenity_ids, ["amenity1", "amenity2"])

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(
                id=None,
                created_at=None,
                updated_at=None,
                city_id=None,
                user_id=None,
                name=None,
                description=None,
                number_rooms=None,
                number_bathrooms=None,
                max_guest=None,
                price_by_night=None,
                latitude=None,
                longitude=None,
                amenity_ids=None
            )


class TestPlace_save(unittest.TestCase):
    """Unittests for testing save method of the Place class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        pl = Place()
        sleep(0.05)
        first_updated_at = pl.updated_at
        pl.save()
        self.assertLess(first_updated_at, pl.updated_at)

    def test_two_saves(self):
        pl = Place()
        sleep(0.05)
        first_updated_at = pl.updated_at
        pl.save()
        second_updated_at = pl.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        pl.save()
        self.assertLess(second_updated_at, pl.updated_at)

    def test_save_with_arg(self):
        pl = Place()
        with self.assertRaises(TypeError):
            pl.save(None)


class TestPlace_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Place class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Place().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        pl = Place()
        self.assertIn("id", pl.to_dict())
        self.assertIn("created_at", pl.to_dict())
        self.assertIn("updated_at", pl.to_dict())
        self.assertIn("__class__", pl.to_dict())

    def test_to_dict_contains_added_attributes(self):
        pl = Place()
        pl.middle_name = "Holberton"
        pl.my_number = 98
        self.assertEqual("Holberton", pl.middle_name)
        self.assertIn("my_number", pl.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        pl = Place()
        pl_dict = pl.to_dict()
        self.assertEqual(str, type(pl_dict["id"]))
        self.assertEqual(str, type(pl_dict["created_at"]))
        self.assertEqual(str, type(pl_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        pl = Place()
        pl.id = "123456"
        pl.created_at = pl.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Place',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(pl.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        pl = Place()
        self.assertNotEqual(pl.to_dict(), pl.__dict__)

    def test_to_dict_with_arg(self):
        pl = Place()
        with self.assertRaises(TypeError):
            pl.to_dict(None)


if __name__ == "__main__":
    unittest.main()
