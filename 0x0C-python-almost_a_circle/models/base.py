#!/usr/bin/python3
"""Defines a Base class"""
import json
import csv


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

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation
        json_string

        args:
            json_string: Is a string representing a list of dictionaries

        Return: an empty list ([]) if json_string  is None or empty
        Otherwise, return the list represented by json_string
        """
        if json_string is None or json_string == []:
            return ([])

        obj_str = json.loads(json_string)
        return (obj_str)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set

        args:
            **dictionary: Can be thought of as a double pointer
            to a dictionary
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                instance = cls(2, 5)  # cls(2, 5, 3)
            elif cls.__name__ == "Square":
                instance = cls(2)  # cls(3, 5, 1)

        instance.update(**dictionary)
        return (instance)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file

        args:
            list_objs: Is a list of instances who inherits of Base
        """
        filename = cls.__name__ + ".json"
        # obj_json = []

        # for obj in list_objs:
        #     obj = cls.to_json_string(obj.to_dictionary())
        #     obj_json.append(json.loads(obj))

        # with open(file_name, "w", encoding="utf-8") as file_n:
        #     json.dump(obj_json, file_n)

        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @classmethod
    def load_from_file(cls):
        """
        Loads the JSON string representation from a file
        """
        filename = cls.__name__ + ".json"

        try:
            with open(filename, "r", encoding="utf-8") as file_a:
                list_dicts = Base.from_json_string(file_a.read())
                return [cls.create(**data) for data in list_dicts]

        except IOError:
            return []

        instance_list = []

        # for instance in data:
        #     obj = cls.create(**instance)
        #     instance_list.append(obj)

        # return (instance_list)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serialize in CSV

        args:
            Pyhton object to serialize
        """
        filename = cls.__name__ + ".csv"

        with open(filename, "w", newline='', encoding="utf-8") as file_a:
            write_to_file = csv.writer(file_a, delimiter=" ")

            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    string = ""
                    obj = obj.to_dictionary()
                    string += (str(obj["id"]) + "," +
                               str(obj["width"]) + "," +
                               str(obj["height"]) + "," +
                               str(obj["x"]) + "," +
                               str(obj["y"]))
                    write_to_file.writerow(string)

            if cls.__name__ == "Square":
                for obj in list_objs:
                    string = ""
                    obj = obj.to_dictionary()
                    string += (str(obj["id"]) + "," +
                               str(obj["size"]) + "," +
                               str(obj["x"]) + "," +
                               str(obj["y"]))
                    write_to_file.writerow(string)

    @classmethod
    def load_from_file_csv(cls):
        """
        DeSerialize in CSV
        """
        return ([])
