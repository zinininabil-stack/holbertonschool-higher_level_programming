#!/usr/bin/python3
"""Module to append text to a file."""


def append_write(filename="", text=""):
    """Appends text to a file and returns the number of characters added."""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
