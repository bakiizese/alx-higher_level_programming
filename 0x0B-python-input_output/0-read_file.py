#!/usr/bin/python3
'''read file'''


def read_file(filename=""):
    '''read'''
    with open(filename, encoding="utf-8") as t:
        print(t.read(), end="")
