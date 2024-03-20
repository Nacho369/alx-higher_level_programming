#!/usr/bin/python3


def uniq_add(my_list=[]):
    new_list = set(my_list)
    summ = 0

    for val in new_list:
        summ = summ + val

    return (summ)
