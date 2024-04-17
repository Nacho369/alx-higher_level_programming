#!/usr/bin/python3
"""
function that reads a text file
"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout
    Returns none
    """
    with open(filename, "r", encoding="utf-8") as file_a:
        print(file_a.read(), end="")
