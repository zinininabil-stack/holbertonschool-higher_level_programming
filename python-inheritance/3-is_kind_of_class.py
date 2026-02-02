#!/usr/bin/python3
"""Module that defines is_same_class function"""

def is_kind_of_class(obj, a_class):
    """Returns True if obj is kind of an instance of a_class
    
    Args:
        obj: object to check
        a_class: class to compare against
        
    Returns:
        True if obj is exactly an instance of a_class or and instance of, False otherwise"""
    
    return type(obj) is a_class or isinstance