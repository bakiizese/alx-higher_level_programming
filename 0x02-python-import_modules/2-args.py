#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    i = len(sys.argv)
    if ar == 1:
        print("{} arguments.".format(ar-1))
    elif ar == 2:
        print("{} arguments:".format(ar-1))
    else:
        print("{} arguments:".format(ar-1))

    for k in range(1, ar):
        print("{}: {}".format(k, sys.argv[k]))
