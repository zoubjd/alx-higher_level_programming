#!/usr/bin/python3
"""a module for a class"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """a methode"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """a method to validate value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
