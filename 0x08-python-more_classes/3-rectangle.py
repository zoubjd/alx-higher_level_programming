#!/usr/bin/python3

"""Define a Rectangle."""


class Rectangle:
    """Initialize a new Rectangle.


    Args:
        width (int or tuple): the tuple containing width and height.
        height (int): The height of the new Rectangle.
    """
    def __init__(self, _width=0, _height=0):
        if isinstance(_width, tuple):
            if len(_width) != 2:
                raise ValueError("Tuple should contain width and height")
            self.__width, self.__height = _width
        else:
            self.__width = _width
            self.__height = _height
        if not isinstance(_height, int):
            raise TypeError("height must be an integer")
        elif _height < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(_width, int):
            raise TypeError("width must be an integer")
        elif _width < 0:
            raise ValueError("width must be >= 0")

    @property
    def width(self):
        """get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Compute the area of the Rectangle."""
        return self.__height * self.__width

    def perimeter(self):
        """Compute the area of the Rectangle."""
        if self.__height == 0 or self.__width == 0:
            return 0
        half_per = self.__height + self.__width
        return 2 * half_per

    def print(self):
        """Print the Rectangle with the '#' character."""
        if self.__height == 0 or self.__width == 0:
            return ""
        return '\n'.join(['#' * self.__width] * self.__height)

    def __str__(self):
        """Return a string representation of the Rectangle."""
        return self.print()
