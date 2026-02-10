#!/usr/bin/python3
"""Serialization utilities using JSON."""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize data and save it to a file."""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Load and deserialize data from a file."""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
