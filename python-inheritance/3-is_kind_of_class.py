#!/usr/bin/python3
"""Module that defines is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of, or inherited from, a_class
    
    Args:
        obj: object to check
        a_class: class to compare against
        
    Returns:
        True if obj is an instance of a_class or inherited from it
    """
    return isinstance(obj, a_class)