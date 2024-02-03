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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value[0], int) or len(value) < 2 or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[1], int) or len(value) < 2 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        return self.size * self.size

    def my_print(self):
        if self.size == 0:
            print()
        for i in range(self.position[1]):
            if i > 0:
                print()
        for i in range(self.size):
            # if not self.position[1] > 0:
            print("_" * self.position[0], end="")
            for i in range(self.size):
                print("#", end="")
            print()
