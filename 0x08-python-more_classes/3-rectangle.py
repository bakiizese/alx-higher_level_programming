#!/usr/bin/python3
'''a real rectangle class'''


class Rectangle:
    '''presenting a rectangle class'''

    def __init__(self, width=0, height=0):
        '''initial rectangle'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''width method'''
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''height method'''
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''return area'''
        return (self.__width * self.__height)

    def perimeter(self):
        '''return perimeter'''
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        '''print #'''
        if self.__width == 0 or self.height == 0:
            return("")
        r = []
        for i in range(self.__height):
            [r.append("#") for k in range(self.__width)]
            if i != self.__height - 1:
                r.append("\n")
        return ("".join(r))
