#!/usr/bin/python3

"""MyList"""


class MyList(list):
    """MyList class"""

    def print_sorted(self):
        """Prints a list in ascending order"""
        print(sorted(self))
