#!/usr/bin/python3

"""
It's a script do define a square
"""


class Square:
    def __init__ (self, size=0):
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("Size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        return (self._Square__size * self._Square__size)

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value: int):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
