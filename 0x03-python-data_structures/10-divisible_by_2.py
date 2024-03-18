#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    new_list = [True if my_list[ind] % 2 == 0 else False for ind, val in enumerate(my_list)]
    return (new_list)
