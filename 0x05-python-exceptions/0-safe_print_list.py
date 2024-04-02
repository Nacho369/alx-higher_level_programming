#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    index = 0
    for ind, val in enumerate(my_list):
        try:
            if (ind < x):
                print(f"{val}", end="")
                index += 1
        except IndexError:
            print()
            return (index)

    print()
    return (index)
