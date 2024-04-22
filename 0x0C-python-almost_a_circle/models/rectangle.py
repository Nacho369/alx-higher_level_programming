#!/usr/bin/python3
"""Defines a Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """
    Represents a Rectangle class that
    inherits from the Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle object

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Returning a 'width' Private attr"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Setting a 'width' Private attr
        Args:
            value: Value to set the 'width' to
        """
        self.setter_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """Returning a 'height' Private attr"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Setting a 'height' Private attr
        Args:
            value: Value to set the 'height' to
        """
        self.setter_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """Returning an 'x' Private attr"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """
        Setting an 'x' Private attr
        Args:
            value: Value to set 'x' to
        """
        self.setter_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """Returning a 'y' Private attr"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """
        Setting a 'y' Private attr
        Args:
            value: Value to set 'y' to
        """
        self.setter_validator("y", value)
        self.__y = value

    def area(self):
        """
        Returns the area of the Rectangle object
        """
        return (self.width * self.height)

    def display(self):
        """
        Prints in stdout the Rectangle
        instance with the character #
        """
        if self.width == 0 or self.height == 0:
            print("")
            return

        # print("\n".join(["#" * self.width for _ in range(self.height)]))

        [print() for _ in range(self.y)]

        for _ in range(self.height):
            [print(" ", end="") for _ in range(self.x)]
            [print("#", end="") for _ in range(self.width)]
            print()

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

        elem = [self.id, self.width, self.height, self.x, self.y]

        for indx, val in enumerate(args):
            elem[indx] = val

        self.id, self.width, self.height, self.x, self.y = elem

    def to_dictionary(self):
        """
        Retrun dictonary representation of a Rectangle
        """
        return ({
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width
        })

    def __str__(self):
        """
        Overrides the __str__ method so it returns a different string
        """
        return (
            f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
            f"{self.width}/{self.height}"
            )

    @staticmethod
    def setter_validator(attr_name, value):
        """
        Validate the setter method
        Args:
            attr_name: Name of the attribute
            value: Value given to the attribute
        """
        if not isinstance(value, int):
            raise TypeError(f"{attr_name} must be an integer")

        if attr_name == "x" or attr_name == "y":
            if value < 0:
                raise ValueError(f"{attr_name} must be >= 0")
        elif value <= 0:
            raise ValueError(f"{attr_name} must be > 0")
