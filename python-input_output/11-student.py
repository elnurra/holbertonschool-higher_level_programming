#!/usr/bin/python3
"""Student to disk and reload"""


class Student:
    """representation of a student"""
    def __init__(self, first_name, last_name, age):
        """instantiation of the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance
        with filter"""
        if (type(attrs) is list and
                all(type(element) is str for element in attrs)):
            new_dict = {}
            for element in attrs:
                if element in self.__dict__:
                    new_dict[element] = self.__dict__[element]
            return (new_dict)
        return (self.__dict__)

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
