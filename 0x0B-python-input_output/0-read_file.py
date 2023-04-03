#!/usr/bin/python3
def read_file(filename=""):
    """function to read text file and print output"""

    with open(filename) as f:
        text = f.read()
        print(text, end="")
