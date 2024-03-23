#!/usr/bin/python3
def common_elements(set_1, set_2):
    comman = []
    for elem in set_1:
        for el in set_2:
            if elem == el:
                comman.append(el)
    return comman
