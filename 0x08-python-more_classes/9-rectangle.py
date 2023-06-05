#!/usr/bin/python3
'''a real rectangle class'''


class Rectangle:
    '''presenting a rectangle class'''

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''initial rectangle'''
        type(self).number_of_instances += 1
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

    @staticmethod
    def bigger__or_equal(rect_1, rect_2):
        '''return the largest area'''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        '''retrun new rec'''
        return (cls(size, size))
    def perimeter(self):
        '''return perimeter'''
        if self.__width == 0 or self.__height == 0:
            return (0)

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

    def __repr__(self):
        '''return string representation'''
        r = "Rectangle(" + str(self.__width)
        r += ", " + str(self.__height) + ")"
        return (r)

    def __del__(self):
        '''print message'''
        type(self).number_of_instances -= 1
        print("Bye rectangle..."
