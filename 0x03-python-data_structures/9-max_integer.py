#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        current_max = 0
        for i in my_list:
            if i > current_max:
                current_max = i
        return current_max
    else:
        return None
