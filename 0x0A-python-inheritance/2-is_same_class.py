#!/usr/bin/python3

"""
This module contains function that checks if the object
pased is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """

    if type(obj) == a.class:
        return True
    return False
