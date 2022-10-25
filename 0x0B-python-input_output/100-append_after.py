#!/usr/bin/python3
""" function that append a new line
"""


def append_after(filename="", search_string="", new_string=""):
    """ function append_after(filename="", search_string="", new_string=""):
    """
    _line = []
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            _line += [line]
            if line.find(search_string) != -1:
                _line += [new_string]

    with open(filename, 'w', encoding="utf-8") as f:
        f.write("".json(_line))
