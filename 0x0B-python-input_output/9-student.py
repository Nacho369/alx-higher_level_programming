#!/usr/bin/python3
""" Defines a class Student that defines a student
"""


class Student:
    """
    A module class student
    """

    def __init__(self, first_name, last_name, age):
        """
        A __init__ method
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        A to_json method
        """
        return (self.__dict__)
