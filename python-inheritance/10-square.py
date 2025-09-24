#!/usr/bin/python3

"""
10-rectangle.py
Write a class Square that inherits
from Rectangle with instantiation
with size: def __init__(self, size)
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Square - Set a square object
    Return: Void
    """
    def __init__(self, size):
        """
       __init__ - Init function with
        Width and Height value
        """
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """
        __str__ - Human 
        output
        """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)

    def area(self):
        """
        area - Calculate the 
        area of the square
        """
        return (self.__size * self.__size)
