#!/usr/bin/python3
"""inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks if an object is"""

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False

