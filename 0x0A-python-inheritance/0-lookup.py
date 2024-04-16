#!/usr/bin/python3

"""Define the lookup() function"""


def lookup(obj):
    """The function returns the list of available attributes and
    methods of an object:

    Args:
        obj: Object which attribute is to be returned

    Return: A list object
    """

    return (dir(obj))
