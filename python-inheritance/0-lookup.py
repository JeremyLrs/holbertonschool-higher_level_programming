#!/usr/bin/python3

"""
0-lookup.py
Write a function that returns the list of
available attributes and methods of an object
Return: A list object
"""


def lookup(obj):
    """
    Look object attribut & methods
    Return: list object
    """
    return dir(obj)
