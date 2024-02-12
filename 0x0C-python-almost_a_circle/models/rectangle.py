#!/usr/bin/python3

"""Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """really... i don't even..."""
        return self.__width

    @width.setter
    def width(self, value):
        """really... i don't even..."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """really... i don't even..."""
        return self.__height

    @height.setter
    def height(self, value):
        """really... i don't even..."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """really... i don't even..."""
        return self.__x

    @x.setter
    def x(self, value):
        """really... i don't even..."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """really... i don't even..."""
        return self.__y

    @y.setter
    def y(self, value):
        """really... i don't even..."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """really... i don't even..."""
        return self.width * self.height

    def display(self):
        """really... i don't even..."""
        if self.width == 0 or self.height == 0:
            print()
            return
        print("\n" * self.__y, end="")
        print("\n".join([" " * self.__x + "#" * self.__width] * self.__height))

    def update(self, *args, **kwargs):
        """really... i don't even..."""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """really... i don't even..."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }

    def __str__(self):
        """really... i don't even..."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )
