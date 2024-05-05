#!/usr/bin/python3
"""a module for a class"""


class Rectangle(BaseGeometry):
    """a class named Rectangle"""
    def __init__(self, width, height):
        """ractagle instatiation"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
