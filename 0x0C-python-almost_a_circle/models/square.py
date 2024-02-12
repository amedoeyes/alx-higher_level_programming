#!/usr/bin/python3

"""Sequare class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """init"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """really... i don't even..."""
        return self.width

    @size.setter
    def size(self, value):
        """really... i don't even..."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """really... i don't even..."""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """really... i don't even..."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }

    def __str__(self):
        """really... i don't even..."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
