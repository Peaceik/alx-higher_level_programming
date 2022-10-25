#!/usr/bin/python3
""" function that returns the dictionary description
"""


def class_to_json(obj):
    """ function class_to_json(obj)
    """
    data = {}
    if hasattr(obj, "__dict__"):
        data = obj.__dict__.copy()
    return data
