#!/usr/bin/python3

"""
9-rectangle.py
Implement Rectangle class
inheriting from BaseGeometry with area
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    setup a rectangle object
    """

    def __init__(self, width, height):
        """
        __init__ - Init function with
        Width and Height value
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def __str__(self):
        """
        __str__ - Human output
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """
        Calculate the area of the recangle
        """
        return (self.__width * self.__height)
