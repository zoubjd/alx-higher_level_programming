#!/usr/bin/python3

"""Define a Rectangle."""

class Rectangle:
    """Initialize a new Rectangle.

    Args:
        width (int or tuple): The width of the new Rectangle. If a tuple is provided, it should contain (width, height).
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
            raise TypeError("size must be an integer ")
        elif _height < 0:
            raise ValueError("size must be >= 0 ")
        self._height = _height
        if not isinstance(_width, int):
            raise TypeError("size must be an integer ")
        elif _width < 0:
            raise ValueError("size must be >= 0 ")
        self._width = _width
        

    @property
    def width(self):
        """get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer ")
        elif value < 0:
            raise ValueError("width must be >= 0 ")
        self.__width = value

    @property
    def height(self):
        """get the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer ")
        elif value < 0:
            raise ValueError("height must be >= 0 ")
        self.__height = value
