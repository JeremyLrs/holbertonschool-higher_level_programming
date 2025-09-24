#!/usr/bin/python3

"""
3-is_kind_of_class.py
Write a function that returns True
if the object is an instance of,
or if the object is an instance of
a class that inherited from,
the specified class ; otherwise False.
Return: True if it is otherwise False
"""


def is_kind_of_class(obj, a_class):
    """
    is_kind_of_class - Compare obj and class
    @obj: An object
    @a_class: A class
    Return: True if obj == a_class, else False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
