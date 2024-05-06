#!/usr/bin/python3
"""a model of a class"""
from models.base import Base


class Rectangle(Base):
    """a class of a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """the class initializer"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Get/set the current size of the rectangle."""
        return (self.__width)

    @width.setter
    def width(self, value):
        self.__size = value

    @property
    def height(self):
        """Get/set the current size of the rectangle."""
        return (self.__height)

    @height.setter
    def width(self, value):
        self.__height = value

    @property
    def x(self):
        """Get/set the current size of the rectangle."""
        return (self.__x)

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """Get/set the current size of the rectangle."""
        return (self.__y)

    @y.setter
    def width(self, value):
        self.__y = value
