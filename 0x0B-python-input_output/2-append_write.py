#!/usr/bin/python3
"""
Dtefines a function that appends to a file
"""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file.
    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as file_a:
        return (file_a.write(text))
