#!/usr/bin/python3
"""A module with a function that reads a text file."""


def read_file(filename=""):
    """This function reads a text file (UTF8) and prints it to stdout"""

    With open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
