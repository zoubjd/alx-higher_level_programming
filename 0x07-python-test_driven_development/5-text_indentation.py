#!/usr/bin/python3
"""Module for add_integer method."""


def text_indentation(text):
    """prints a text

    Args:
        text: the text.

    Raises:
        TypeError: if text is not string.

    """
    split_chars = ['.', '?', ':']

    for char in text:
        print(char, end='')

        if char in split_chars:
            print('\n\n', end='')
    print()

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
