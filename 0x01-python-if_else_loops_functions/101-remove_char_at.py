#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = str
    for i in range(len(new_str)):
        if i == n:
            new_str = new_str.replace(new_str[i], "", 1)
    return new_str
