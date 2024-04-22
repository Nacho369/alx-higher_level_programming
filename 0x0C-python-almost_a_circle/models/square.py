#!/usr/bin/python3
"""Defines a sqaure class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Rrepresents a Sqaure class that
    inherits from a rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize an instance of a Sqaure class that
        inherits from a Rectangle class
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Returning a 'size' attribute"""
        return (self.width)

    @size.setter
    def size(self, value):
        """
        Setting a 'size' attribute

        args:
            value: Value to be assigned
        """
        self.width = value

    def update(self, *args, **kwargs):
        """
        Update the class Rectangle and assigns
        an argument to each attribute

        args:
            *args: Variable number of arguments to be passed
            **kwargs: Variable number of key/value args to be passed
        """
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        elem = [self.id, self.width, self.x, self.y]

        for indx, val in enumerate(args):
            elem[indx] = val

        self.id, self.width, self.x, self.y = elem

    def to_dictionary(self):
        """
        Retrun dictonary representation of a Rectangle
        """
        return ({
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        })

    def __str__(self):
        """
        Overrides the __str__ method so it returns a different string
        """
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")
