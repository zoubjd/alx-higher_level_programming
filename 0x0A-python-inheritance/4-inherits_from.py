#!/usr/bin/python3
"""CHEcks for weither """


def inherits_from(obj, a_class):
    """returns true if obj and a_classe are the same
    Args:
    a: the object
    a_class: the class to be tested

    Return: True or False
    """

    return isinstance(obj, a_class) and type(obj) != a_class
