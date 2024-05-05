#!/usr/bin/python3
"""a module for Rectang"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a class named Square"""

    def __init__(self, size):
        """square instatiation"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """a methode"""
        return self.__size * self.__size
