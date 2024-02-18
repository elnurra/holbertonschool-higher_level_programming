from models.base import Base
import os
import json

import unittest


class TestBase(unittest.TestCase):
    """Documentation"""
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_init(self):
        """Test automatic id assignment."""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(89)
        self.assertEqual(b2.id, 89)

    def test_to_json_string(self):
        """Test converting list of dictionaries to JSON string."""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')

    def test_from_json_string(self):
        """Test converting JSON string to list."""
        json_str = '[{"id": 1}, {"id": 2}]'
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string('[{"id": 89}]'), [{'id': 89}])
        self.assertEqual(Base.from_json_string(json_str), [{"id": 1}, {"id": 2}])

    def test_save_to_file(self):
        """Test saving None to file."""
        Base.save_to_file(None)
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        os.remove("Base.json")  # Clean up


if __name__ == '__main__':
    unittest.main()
