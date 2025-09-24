#!/usr/bin/python3

"""
1-my_list.py
Write a class MyList that inherits from list
Return: subclass
"""


class MyList(list):
    """
    MyList - Define list methods
    @list - Inherits from list
    Return a subclass
    """
    def print_sorted(self):
        sorted = self.copy()
        sorted.sort()
        print(sorted)
