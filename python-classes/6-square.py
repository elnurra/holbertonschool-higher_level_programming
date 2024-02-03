#!/usr/bin/python3
"""A class Square that defines a square by: (based on 2-square.py)"""


class Square:
    """A class that defines and initializes an instance

    Attributes:
        __size: size of the instance
        __position: position of the instance
    Methods:
        __init__: initializes the instance of the class
        area: computes the area of the instance
        my_print: prints the square at a given position
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
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not isinstance(value[0], int)
            or not isinstance(value[1], int)
            or value[0] < 0
            or value[1] < 0
        ):
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
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                print(" " * self.position[0], end="")
                for j in range(self.size):
                    print("#", end="")
                print()


if __name__ == "__main__":
    try:
        my_square = Square(3, (1, ))
        my_square.my_print()
    except Exception as e:
        print(e)
