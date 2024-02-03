#!/usr/bin/python3
"""a class Square that defines a square by: (based on 2-square.py)"""


class Square:
    """a classs that defines and initializes an instance


    Attributes:
        __size: size of the instance
    methods:
        __init__: initialises the instance of the class
        area: computes the area of the instance
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            self.size = size

    def area(self):
        return self.size * self.size
