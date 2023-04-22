#!/usr/bin/python3

"""
This module contains function that checks if the object
passed is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """Implements sorted printing for the built-in list class."""

    return type(obj) == a_class
