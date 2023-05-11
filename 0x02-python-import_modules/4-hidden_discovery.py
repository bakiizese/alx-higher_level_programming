#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    num = dir()
    ln = len(num)
    for i in range(0, ln):
        if num[i][0:2] != "__":
            print("{}".format(num[i]))
