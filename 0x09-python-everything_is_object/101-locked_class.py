#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    allow the user to onyl have an attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
