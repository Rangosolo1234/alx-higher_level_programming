#!/usr/bin/python3
"""-------------------------------"""


def append_write(filename="", text=""):
    """Appends a string to the end of textfile.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
