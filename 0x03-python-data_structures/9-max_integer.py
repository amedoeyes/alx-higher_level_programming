#!/usr/bin/python3


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    max_int = my_list[0]
    for n in my_list:
        max_int = n if n > max_int else max_int

    return max_int
