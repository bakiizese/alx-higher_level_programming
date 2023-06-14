#!/usr/bin/python3
'''write file'''


def write_file(filename="", text=""):
    '''write'''
    with open(filename, 'w', encoding="utf-8") as wr:
        return wr.write(text)
