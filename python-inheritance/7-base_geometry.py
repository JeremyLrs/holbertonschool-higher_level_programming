#!/usr/bin/python3

"""
5-base_geometry.py
Create an empty class BaseGeometry
"""


class BaseGeometry():
    """
    Empty class BaseGeometry
    """
    def area(self):
        """
        area is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        check if is an int and the value is > 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
