#!/usr/bin/python3

"""
A module function that writes an Object to a text
file, using a JSON representation
"""

import json


def save_to_json_file(my_obj, filename):
    """json representation of an object string"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
