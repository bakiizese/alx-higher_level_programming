#!/usr/bin/python3
'''append text'''


def append_write(filename="", text=""):
    '''append'''
    with open(filename, 'a', encoding="utf-8") as ap:
        return ap.write(text)
