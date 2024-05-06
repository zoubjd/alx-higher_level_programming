#!/usr/bin/python3
"""a model of a class"""


class Base:
    """a class named base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """a class constructor"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def get_id(self):
        """a method to get the id attribute"""
        return self.__id

