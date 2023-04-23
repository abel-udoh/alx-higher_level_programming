#!/usr/bin/python3

"""
This module contains a function that defines
a JSON-to-object function.
"""

import json


def from_json_string(my_str):
    """Return the Python object representation of a JSON string."""
    return json.loads(my_str)
