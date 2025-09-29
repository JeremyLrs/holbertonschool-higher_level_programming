#!/usr/bin/python3

'''
0-read_file.py
Function to read a file.
'''


def read_file(filename=""):
    '''
    Funtion for read a file and printing content
    '''
    with open(filename, 'r', encoding="uts-8") as f:
        read_data = f.readline()
        while read_data != "":
            print(read_data, end="")
            read_data = f.readline()
