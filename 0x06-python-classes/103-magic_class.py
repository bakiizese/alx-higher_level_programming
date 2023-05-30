#!/usr/bin/python3

"""Define a MagicClass matching exactly a bytecode provided by Holberton."""

import math


class MagicClass:
    """Represent a circle."""

    def __init__(self, rd=0):
        """Initialize a MagicClass.
        Arg:
            rd (float or int): The radius of the new MagicClass.
        """
        self.__rd = 0
        if type(rd) is not int and type(rd) is not float:
            raise TypeError("radius must be a number")
        self.__rd = rd

    def area(self):
        """Return the area of the MagicClass."""
        return (self.__rd ** 2 * math.pi)

    def circumference(self):
        """Return The circumference of the MagicClass."""
        return (2 * math.pi * self.__rd)
