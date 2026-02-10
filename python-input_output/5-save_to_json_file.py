#!/usr/bin/python3
"""Module that defines save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file using JSON representation
    
    Args:
        my_obj: Python object to serialize
        filename (str): path to the file to write
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return json.dump(my_obj, f)
