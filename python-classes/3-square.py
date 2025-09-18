#!/usr/bin/python3

"""
It's a script do define a square
"""


class Square:
    """
    Define a square
    """
    def __init__(self, size=0):
        """
        __init__ - Init new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        area - Calculate square area
        """
        return (self._Square__size * self._Square__size)
