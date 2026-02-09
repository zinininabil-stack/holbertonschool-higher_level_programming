#!/usr/bin/python3
"""Module that defines a Student class"""


class Student:
    """Represents a student with first name, last name, and age"""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance
        
        Args:
            first_name (str): first name of the student
            last_name (str): last name of the student
            age (int): age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance
        
        Args:
            attrs (list): list of attribute names to retrieve (optional)
            
        Returns:
            dict: dictionary containing requested attributes or all attributes
        """
        if attrs is None:
            return self.__dict__
        
        new_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                new_dict[attr] = getattr(self, attr)
        return new_dict
