#!/usr/bin/python3
"""
Defines a Save Object to a file function
"""
import json


def save_to_json_file(my_obj, filename):
    """
    A function that writes an Object to a text file,
    using a JSON representation

    Args:
        my_obj: Object file
        filename: File to write to
    """
    json_str = json.dumps(my_obj)

    with open(filename, "w", encoding="utf-8") as file_a:
        file_a.write(json_str)
