#!/usr/bin/python3

'''
1-write_file.py
Function to writes a string to a text file.
'''


def write_file(filename="", text=""):
    '''
    Function to write a string and
    return the number of char written
    '''

    with open(filename, 'w', encoding="utf-8") as f:
        write_data = f.write(text)

        return write_data
