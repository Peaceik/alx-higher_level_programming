#!/usr/bin/python3
""" defines a class Student
"""


class Student:
    """ create class Student with instance
    """

    def __init__(self, first_name, last_name, age):
        """ initializing class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ method to return directory description"""
        return self.__dict__.copy()
