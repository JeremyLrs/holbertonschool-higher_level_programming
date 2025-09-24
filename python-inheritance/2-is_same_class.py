#!/usr/bin/python3

"""
2-is_same_class.py
Write a function that returns True
if the object is exactly an instance
of the specified class ; otherwise False.
Return: True if it is otherwise False
"""


def is_same_class(obj, a_class):
    """
    is_same_class - Check if obj is the same as a_class
    @obj: An object
    @a_class: A class
    Return: True if obj == a_class, else False
    """
    if type(obj) is a_class:
        return True
    else:
        return False
