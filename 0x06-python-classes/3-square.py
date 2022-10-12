#!/usr/bin/python3
""" defines class"""


class Square:
    """ class square that defines a square.
    """
    def __init__(self, size=0) -> None:
        """ Method to initialize
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Method to return area
        """
        return (self.__size ** 2)
