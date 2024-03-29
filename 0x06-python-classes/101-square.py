#!/usr/bin/python3

"""Square"""


class Square:
    """Square"""

    __size = 0
    __position = (0, 0)

    def __init__(self, size=0, position=(0, 0)):
        """Square"""
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (
            type(value) is not tuple
            or len(value) != 2
            or type(value[0]) is not int
            or value[0] < 0
            or type(value[1]) is not int
            or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()

    def __str__(self):
        if self.__size == 0:
            return ""

        str = ""

        for i in range(self.__position[1]):
            str += "\n"

        for i in range(self.__size):
            for k in range(self.__position[0]):
                str += " "
            for j in range(self.__size):
                str += "#"
            if i != self.__size - 1:
                str += "\n"

        return str
