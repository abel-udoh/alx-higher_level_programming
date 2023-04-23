#!/usr/bin/python3

"""
This module contains function that returns the
JSON representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """returns JSON representation"""

    return json.dumps(my_obj)
