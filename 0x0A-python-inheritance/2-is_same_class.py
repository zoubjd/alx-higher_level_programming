#!/usr/bin/python3
"""CHEcks for weither """


def is_same_class(obj, a_class):
    """returns true if obj and a_classe are the same
    Args:
    a: the object
    a_class: the class to be tested

    Return: True or False
    """

    return type(obj) == a_class
