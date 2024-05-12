#!/usr/bin/python3
"""a model of a class"""
from models.base import Base


class Rectangle(Base):
    """A class representing a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle instance."""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def integer_validator(self, name, value):
        """a method to validate value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if name == "x" or name == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))
        else:
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """Get/set the x-coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        self.integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """Get/set the y-coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        self.integer_validator("y", value)
        self.__y = value
