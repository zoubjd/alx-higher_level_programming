#!/usr/bin/python3
file = open("thezen.txt", 'r')
for ch in file:
    if ch == ".":
        print(".\n")
    print(ch, end="")