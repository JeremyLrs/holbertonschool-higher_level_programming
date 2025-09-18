#!/usr/bin/python3

"""
It's a script do define a square
"""


class Square:
    """
    Define a square
    """
    def __init__(self, size: int = 0, position: tuple = (0, 0)):
        """
        __init__ - Init new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size

        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        
        elif not isinstance(position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        
        elif not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        
        self.__position = position

    def area(self):
        """
        area - Calculate square area
        """
        return (self._Square__size * self._Square__size)

    @property
    def size(self):
        """
        size - Get size of the square
        """
        return self.__size

    @size.setter
    def size(self, value: int):
        """
        size - Set the size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        position - Get square position
        """
        return self.__position

    @position.setter
    def position(self, value: tuple):
        """
        position - Set square position
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        
        self.__position = value

    def my_print(self):
        """
        my_print - Print # square
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for offset in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()