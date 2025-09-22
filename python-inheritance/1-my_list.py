#!/usr/bin/python3

"""
1-my_list.py
Write a class MyList that inherits from list
Return: subclass
"""


class MyList(list):
    def print_sorted(self):
        print(sorted(self))
