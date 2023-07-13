#!/usr/bin/python3
""" a class Square that inherits from Rectangle """
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ class square from class Rectangle """

    def __init__(self, size):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
