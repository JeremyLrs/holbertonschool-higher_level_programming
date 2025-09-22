#!/usr/bin/python3

"""
8-rectangle.py
Define Rectangle that inherits from BaseGeometry
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
