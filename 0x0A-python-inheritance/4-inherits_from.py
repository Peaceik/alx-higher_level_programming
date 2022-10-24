#!/usr/bin/python3
""" function inherits_from
"""


def inherits_from(obj, a_class):
    """ defines a function
    """
    if type(obj) is a_class:
        return False

    return isinstance(obj, a_class)
