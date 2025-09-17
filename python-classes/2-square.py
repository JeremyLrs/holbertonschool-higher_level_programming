#!/usr/bin/python3

"""
It's a script do define a square class
with :  Private instance attribute: size
"""


class Square:
    def __init__ (self, size=0):
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("Size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
