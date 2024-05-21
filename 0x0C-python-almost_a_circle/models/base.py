#!/usr/bin/python3
"""Defines a Base class"""
import json
import csv
import turtle


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
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        DeSerialize in CSV
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
