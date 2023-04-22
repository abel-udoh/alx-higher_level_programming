#!/usr/bin/python3

"""
This module appends a string to a file
and print out the text added
"""


def append_write(filename="", text=""):
    """append a string and print the output"""

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
