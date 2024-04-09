#!/usr/bin/python3

"""Define a function to print 'My name is <first name> <last name>'"""


def say_my_name(first_name, last_name=""):
    """
    The function prints "My name is <first name> <last name>" ending with a new
    line
    Args:
        first_name(str): First name to be passed
        last_name(str): Last name to be passed
    Raises:
        TypeError: If firstname or lastname is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name == "":
        print("My name is {}".format(first_name, last_name))
    else:
        print("My name is {} {}".format(first_name, last_name))