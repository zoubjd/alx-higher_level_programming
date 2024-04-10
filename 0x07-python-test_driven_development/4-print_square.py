#!/usr/bin/python3
"""Module for print_square method."""


def print_square(size):
    """prints a square

    Args:
        size: the size of the square.

    Raises:
        TypeError: if size is not int.
        TypeError: if size is a float and less than 0
        ValueError: if size is less than 0

    """
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print("")
    for _ in range(size):
        print("#" * size)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
