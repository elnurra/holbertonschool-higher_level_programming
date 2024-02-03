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
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __init__(self, size=0):
        self.size = size

    def area(self):
        return self.size * self.size

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                for i in range(self.size):
                    print("#", end="")
                print()
