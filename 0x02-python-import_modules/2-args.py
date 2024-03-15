#!/usr/bin/python3

if __name__ == "__main__":
    """print the arguments"""
    import sys

    count = len(sys.argv)
    if count == 1:
        print("0 arguments.")
    elif count == 2:
        print("1 argument:")
        print("{}: {}".format(count - 1, sys.argv[1]))
    else:
        print("{}: arguments:".format(count))
        for i in sys.argv:
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
