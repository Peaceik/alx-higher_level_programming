#!/usr/bin/python3
""" defines class Rectangle
"""


class Rectangle(BaseGeometry):
    """ class Rectangle that inherits BaseGeometry
    """
    def __init__(self, width, height):
        """ initializing function of the class Rectangle
        """
        self.integer_validator("width" width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
