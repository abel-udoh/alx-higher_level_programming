#!/usr/bin/python3

"""
This module contains functions that reads a text file and prints
it to stdout
"""


def read_file(filename=""):
    """This function reads a text file (UTF8) and prints it to stdout"""

    With open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
