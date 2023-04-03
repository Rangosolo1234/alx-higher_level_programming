#!/usr/bin/python3
"""
===============================
--------------------------------
"""


def write_file(filename="", text=""):
    """ function to write file
    """
    with open(filename, 'w') as f:
        return f.write(text)
