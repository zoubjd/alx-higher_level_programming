#!/usr/bin/python3
"""module for MyList class"""


class MyList(list):
    """MyList class"""
    def print_sorted(self):
        """printing in soer"""
        print(sorted(self))
