#!/usr/bin/python3
for i in range(99):
    if i < 10:
        i = '0' + str(i)
    print(i, end=', ')
print("99\n")