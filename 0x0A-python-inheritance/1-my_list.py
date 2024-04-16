#!/usr/bin/python3

"""Define a class MyList"""


class MyList(list):
    """Class that inherita from list"""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        print(sorted(self))
