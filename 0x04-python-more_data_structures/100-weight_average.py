#!/usr/bin/python3


def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return (0)

    t_weight = 0
    t_num = 0

    for x, y in my_list:
        t_weight += x * y
        t_num += y
    return (t_weight / t_num)
