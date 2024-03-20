#!/usr/bin/python3


def search_replace(my_list, search, replace):
    new_list = my_list[:]

    for ind, elem in enumerate(new_list):
        if elem == search:
            new_list[ind] = replace

    return (new_list)
