#!/usr/bin/python3
"""
Defines a To JSON string Function
"""
import json


def to_json_string(my_obj):
    """
    A  function that returns the JSON representation of an object (string)

    Args:
        my_obj: Object string
    """
    return (json.dumps(my_obj))
