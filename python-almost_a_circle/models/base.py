#!/usr/bin/python3
"""Defines a Base class."""


import json
import turtle


class Base:
    """Base class for managing id attribute."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new instance with a given id."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # Create a dummy Rectangle instance
        elif cls.__name__ == "Square":
            dummy = cls(1)  # Create a dummy Square instance
        else:
            return None
        dummy.update(**dictionary)  # Update dummy instance with real values
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a JSON file."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_data = file.read()
        except FileNotFoundError:
            return []

        list_dicts = cls.from_json_string(json_data)
        return [cls.create(**d) for d in list_dicts]

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            file.write(cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of dictionaries represented by json_string."""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @staticmethod
    def draw(list_rectangles, list_squares):
        # Initialize the turtle screen
        screen = turtle.Screen()
        screen.title("Shapes Drawing")
        screen.setup(width=800, height=600)

        # Create a turtle object
        pen = turtle.Turtle()
        pen.speed(0)  # Set the drawing speed to the fastest

        # Draw rectangles
        for rectangle in list_rectangles:
            pen.penup()
            pen.goto(rectangle.x, rectangle.y)
            pen.pendown()
            pen.color("blue")  # Set color for rectangles
            pen.begin_fill()
            for _ in range(2):
                pen.forward(rectangle.width)
                pen.left(90)
                pen.forward(rectangle.height)
                pen.left(90)
            pen.end_fill()

        # Draw squares
        for square in list_squares:
            pen.penup()
            pen.goto(square.x, square.y)
            pen.pendown()
            pen.color("red")  # Set color for squares
            pen.begin_fill()
            for _ in range(4):
                pen.forward(square.size)
                pen.left(90)
            pen.end_fill()

        # Hide the turtle and display the drawing
        pen.hideturtle()
        screen.mainloop()
