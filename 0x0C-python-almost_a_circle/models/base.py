#!/usr/bin/python3
"""Defines a Base class"""
import json


class Base:
    """Represent a Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initaializes an instance of the Base class

        Args:
            id: Public instance attr of Base class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation
        of list_dictionaries

        args:
            list_dictionaries: Is a list of dictionaries

        Return: "[]" if list_dictionaries is None or empty
        Otherwise, return the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")

        json_str = json.dumps(list_dictionaries)
        return (json_str)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file

        args:
            list_objs: Is a list of instances who inherits of Base
        """
        file_name = cls.__name__ + ".json"
        obj_json = []

        for obj in list_objs:
            obj = cls.to_json_string(obj.to_dictionary())
            obj_json.append(json.loads(obj))

        with open(file_name, "w", encoding="utf-8") as file_n:
            json.dump(obj_json, file_n)
