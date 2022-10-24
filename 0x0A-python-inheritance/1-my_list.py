#!/usr/bin/python3
""" defines class Mylist
"""


class Mylist(list):
    """ class that inherits from list
    """

    def print_sorted(self):
        """ func print_sorted
        """
        print(sorted(self))
