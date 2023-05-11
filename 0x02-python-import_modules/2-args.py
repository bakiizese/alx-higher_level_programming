#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    i = len(sys.argv)
    if i == 1:
        print("{} arguments.".format(i-1))
    elif i == 2:
        print("{} arguments:".format(i-1))
    else:
        print("{} arguments:".format(i-1))
    for j in range(1, i):
        print(f"{j}: {sys.argv[j]}")
