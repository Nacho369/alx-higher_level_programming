#!/usr/bin/python3
"""Defines a function that creates
object from a JSON file"""
import json


def load_from_json_file(filename):
    """
    A function that creates an Object from a “JSON file”
    """
    with open(filename, "r", encoding="utf-8") as file_a:
        return (json.load(file_a))
