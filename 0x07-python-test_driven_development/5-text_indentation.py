#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    '''text indent'''
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    a = 0
    while a < len(text) and text[a] == ' ':
        a += 1

    while a < len(text):
        print(text[a], end="")
        if text[a] == "\n" or text[a] in ".?:":
            if text[a] in ".?:":
                print("\n")
            a += 1
            while a < len(text) and text[a] == ' ':
                a += 1
            continue
        a += 1
