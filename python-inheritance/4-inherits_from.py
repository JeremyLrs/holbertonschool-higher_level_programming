#!/usr/bin/python3

"""
4-inherits_from.py
Write a function that returns True if
the object is an instance of a class
that inherited (directly or indirectly)
from the specified class ; otherwise False
Return: True if it is otherwise False
"""


def inherits_from(obj, a_class):
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False