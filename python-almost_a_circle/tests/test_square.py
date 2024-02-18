#!/usr/bin/python3


import unittest
from models.square import Square
from unittest.mock import patch
from io import StringIO
import os


class TestSquare(unittest.TestCase):

    def setUp(self):
        """Instances for Square"""
        self.s1 = Square(1)
        self.s2 = Square(1, 2)
        self.s3 = Square(1, 2, 3)
        self.s4 = Square(1, 2, 3, 4)
        self.new_dicts = {"id": 2, "size": 2, "x": 2, "y": 2}
        self.list_s1 = [self.s1]

    def test_checker(self):
        self.assertEqual(self.s1.size, 1)
        self.assertEqual(self.s2.x, 2)
        self.assertEqual(self.s3.y, 3)
        self.assertEqual(self.s4.id, 4)

        """Type Error"""
        with self.assertRaises(TypeError):
            Square("1")
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

        """Value Error"""
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(1, 2, -3)
        with self.assertRaises(ValueError):
            Square(0)

    def test_str(self):
        self.assertEqual(str(self.s4), "[Square] (4) 2/3 - 1")

    def test_to_dictionary(self):
        self.assertEqual(self.s4.to_dictionary(), {"id": 4, "size": 1, "x": 2, "y": 3})

    def test_update(self):
        self.s4.update(2, 4, 7, 8)
        self.assertEqual(str(self.s4), "[Square] (2) 7/8 - 4")

    def test_create(self):
        new = Square.create(**self.new_dicts)
        self.assertEqual(str(new), "[Square] (2) 2/2 - 2")

    def test_save_to_file1(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file2(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file3(self):
        Square.save_to_file([Square(1, id=1)])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), '[{"id": 1, "size": 1, "x": 0, "y": 0}]')
    
    def test_load_from(self):
        self.assertEqual(Square.load_from_file(), [])

        Square.save_to_file(self.list_s1)
        self.assertEqual(self.list_s1[0].__str__(), Square.load_from_file()[0].__str__())

    def tearDown(self):
        try:
            os.remove("Square.json")
        except:
            pass
