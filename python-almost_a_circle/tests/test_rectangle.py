"""Unit test for Rectangle"""
import unittest
from models.rectangle import Rectangle
from io import StringIO
import sys
import os
import json

class TestRectangle(unittest.TestCase):
    """TestCase for Rectangle class"""
    def test_init(self):
        """Initialization case"""
        r1 = Rectangle(10, 20)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_setters(self):
        """"Setters test"""
        r1 = Rectangle(10, 20)
        r1.width = 30
        r1.height = 40
        r1.x = 50
        r1.y = 60
        self.assertEqual(r1.width, 30)
        self.assertEqual(r1.height, 40)
        self.assertEqual(r1.x, 50)
        self.assertEqual(r1.y, 60)

    def test_area(self):
        """Area Function test"""
        r1 = Rectangle(10, 20)
        self.assertEqual(r1.area(), 200)

    def test_update(self):
        """"Update func test"""
        r1 = Rectangle(10, 20)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)

    def test_wrong_init(self):
        """Wrong type of Initialization"""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_str(self):
        self.assertEqual(str(Rectangle(10, 20, 10, 10, 2)), "[Rectangle] (2) 10/10 - 10/20")

    def test_display(self):
        r = Rectangle(2, 2, 2, 2)
        expected_output = "\n\n  ##\n  ##\n"
        output = StringIO()
        sys.stdout = output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), expected_output)

    def test_display_without_x_and_y(self):
        r = Rectangle(2, 2)
        expected_output = "##\n##\n"
        output = StringIO()
        sys.stdout = output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), expected_output)

    def test_display_without_y(self):
        r = Rectangle(2, 2, 2)
        expected_output = "  ##\n  ##\n"
        output = StringIO()
        sys.stdout = output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), expected_output)

    def test_to_dictionary(self):
        r1 = Rectangle(10, 20, 1, 2, 89)
        self.assertEqual(r1.to_dictionary(), {'id': 89, 'width': 10, 'height': 20, 'x': 1, 'y': 2})

    def test_create(self):
        rect_dict = {'id': 89, 'width': 10, 'height': 20, 'x': 2, 'y': 3}
        rect = Rectangle.create(**rect_dict)
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)

    def test_save_to_file_None(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_empty(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", mode="r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file(self):
        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(json.loads(file.read()), [r.to_dictionary()])

    def test_load_from_file_non_existent_file(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_existent_file(self):
        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        rectangles = Rectangle.load_from_file()
        self.assertEqual(len(rectangles), 1)
        self.assertEqual(rectangles[0].to_dictionary(), r.to_dictionary())

    def tearDown(self):
        """This method is called after each test"""

        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

if __name__ == '__main__':
    unittest.main()
