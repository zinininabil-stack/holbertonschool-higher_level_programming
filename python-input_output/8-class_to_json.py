#!/usr/bin/python3
"""Module that defines class_to_json function"""


def class_to_json(obj):
    """Returns the dictionary description for JSON serialization of an object
    
    Args:
        obj: instance of a Class
        
    Returns:
        dict: dictionary with simple data structure (list, dict, str, int, bool)
    """
    return obj.__dict__