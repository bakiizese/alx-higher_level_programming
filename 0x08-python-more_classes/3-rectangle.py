#!/usr/bin/python3
'''a real rectangle'''


class Rectangle:
    ''''preseintg'''

    def __init__(self, width=0, height=0):
        '''initial'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''width;;;'''
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''eight'''
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''return area;'''
        return (self.__width * self.__height)

    def perimeter(self):
        '''return perimeter'''
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ('')
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end='')
            if i != self.__height - 1:
                print('')
        return ('')
