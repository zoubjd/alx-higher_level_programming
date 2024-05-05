#!/usr/bin/python3
"""a module for Rectang"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a class named Rectangle"""

    def __init__(self, width, height):
        """ractagle instatiation"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """a methode"""
        return self.__height * self.__width

    def __str__(self):
        """string representation methode"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)