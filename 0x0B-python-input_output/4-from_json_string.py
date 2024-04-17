#!/usr/bin/python3
"""
Defines a JSON string to object function
"""
import json


def from_json_string(my_str):
    """
    A function that returns an object (Python data structure)
    represented by a JSON string

    Args:
        my_str(str): String object
    """
    return (json.loads(my_str))
