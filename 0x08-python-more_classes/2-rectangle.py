#!/usr/bin/python3


"""
This module contains a class that defines a Rectangle with
private attribute width
"""


class Rectangle:
    """This class defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """This method initializes the class instance
        Args:
            width: The width of the rectangle
            height: The height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """This method retrieves the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """This method set the new value of the width
        Args:
            value: The new width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        else:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

    @property
    def height(self):
        """This method retrieves the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """This method set the new value of the height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        else:
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value

    def area(self):
        """This returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """This returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
