#!/usr/bin/python3

"""Define a class Rectangle."""


class Rectangle:
    """Initialize a new Rectangle.

    Args:
        width (int or tuple): The width of the new Rectangle. If a tuple is provided, it should contain (width, height).
        height (int): The height of the new Rectangle.
    """
    def __init__(self, width=0, height=0):

        if isinstance(width, tuple):
            if len(width) != 2:
                raise ValueError("Tuple should contain width and height")
            self.width, self.height = width
        else:
            self.width = width
            self.height = height


        @property
        def width(self):
            """get the size"""
            return (self.__width)

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            self.__width = value

        @property
        def height(self):
            """get the size"""
            return (self.__height)

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            self.__height = value
