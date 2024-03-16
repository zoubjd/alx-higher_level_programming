#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    result = 0
    count = len(sys.argv) - 1
    if count == 0:
        print("0")
    else:
        for i in range(count):
            result += int(sys.argv[i + 1])
        print("{}".format(result))
