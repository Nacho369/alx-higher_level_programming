#!/usr/bin/python3


def max_integer(my_list=[]):
    if (len(my_list) == 0):
        return (0)

    max_int = 0
    for val in my_list:
        if (val > max_int):
            max_int = val

    return (max_int)
