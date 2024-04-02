#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    ind = 0
    for val in range(x):
        try:
            print("{:d}".format(my_list[val]), end="")
            ind += 1
        except (TypeError, ValueError):
            continue
            return (ind)

    print()
    return (ind)
