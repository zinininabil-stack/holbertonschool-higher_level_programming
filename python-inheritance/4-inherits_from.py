#!/usr/bin/python3
"""Module that defines is_kind_of_class function"""


def inherits_from(obj, a_class):
    """Method to check if object is an instance of a a class"""
    return isinstance(obj, a_class) and type(obj) is not a_class
