#!/usr/bin/python3
"""Module that defines is_same_class function"""


def is_same_class(obj, a_class):
    """Returns True if obj is exactly an instance of a_class
    
    Args:
        obj: object to check
        a_class: class to compare against
        
    Returns:
        True if obj is exactly an instance of a_class, False otherwise
        
    Example:
        >>> is_same_class(1, int)
        True
        >>> is_same_class(1, float)
        False
    """
    return type(obj) is a_class
