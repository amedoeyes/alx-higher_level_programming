#!/usr/bin/python3

"""MyInt class"""


class MyInt(int):
    """Class MyInt"""

    def __eq__(self, value):
        return self.real != value

    def __ne__(self, value):
        return self.real == value
