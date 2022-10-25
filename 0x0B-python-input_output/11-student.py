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

    def to_json(self, attrs=None):
        """ method to return directory description"""
        obj = self.__dict__.copy()
        if type(attrs) is list:

            for item in attrs:
                if type(item) is not str:
                    return obj

            _list = {}

            for iatr in range(len(attrs)):
                for satr in obj:
                    if attrs[iatr] == satr:
                        _list[satr] = obj[satr]
            return _list

        return obj

    def reload_from_json(self, json):
        """ method that replaces all attributes of the Student instance"""
        for atr in json:
            self.__dict__[atr] = json[atr]
