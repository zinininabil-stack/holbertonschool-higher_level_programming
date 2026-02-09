#!/usr/bin/python3
"""Module that defines load_from_json_file function"""
import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file
    
    Args:
        filename (str): path to the JSON file to read
        
    Returns:
        Python object represented by the JSON file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
