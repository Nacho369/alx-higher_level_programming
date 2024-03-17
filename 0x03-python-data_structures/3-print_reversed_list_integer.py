#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if my_list:
        rev = my_list.copy()
        rev.reverse()

        for val in rev:
            print("{:d}".format(val))
