#!/usr/bin/python3
"""Module that defines write_file function"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number of characters written
    
    Args:
        filename (str): path to the file to write (default: "")
        text (str): text to write to the file (default: "")
        
    Returns:
        int: number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
