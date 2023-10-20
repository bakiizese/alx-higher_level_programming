#!/usr/bin/python3
"""class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize new"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """the print() and str()"""
        a = ("[Rectangle] {}/{}".format(self.__width, self.__height))
        return a
