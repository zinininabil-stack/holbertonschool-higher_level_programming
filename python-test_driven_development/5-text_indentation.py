#!/usr/bin/python3
"""
Module for text indentation.
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each '.', '?', ':'.

    Args:
        text: String to format

    Raises:
        TypeError: If text is not a string
    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Process each character
    i = 0
    while i < len(text):
        if text[i] in ".?:":
            print(text[i])
            print()
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
        else:
            print(text[i], end="")
            i += 1
