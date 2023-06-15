#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import unittest
import warnings


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        new.name = str(new.name)
        self.assertEqual(type(new.name), str)


class TestAmenity(unittest.TestCase):
    def test_save(self):
        a = Amenity(name="test")
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            a.save()
        self.assertIsNotNone(a.id)
        self.assertIsNotNone(a.created_at)
        self.assertIsNotNone(a.updated_at)
