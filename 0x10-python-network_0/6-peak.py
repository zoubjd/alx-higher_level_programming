#!/usr/bin/python3
"""finds the peak """


def find_peak(list_of_integers):
    """finds the peak"""
    if list_of_integers == []:
        return
    max = list_of_integers[0]
    for i in list_of_integers:
        if i > max:
            max = i
    return max
