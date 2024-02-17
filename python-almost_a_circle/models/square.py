#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle."""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square instance."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size."""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns a string representation of the Square instance."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    def update(self, *args, **kwargs):
        """Assigns attributes to the Square instance."""
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for attr, val in zip(attrs, args):
                setattr(self, attr, val)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
