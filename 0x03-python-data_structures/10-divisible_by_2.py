#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    bool_list = []
    for i in range(len(my_list)):
        bool_list.append(True if my_list[i] % 2 == 0 else False)
    return bool_list
