#!/usr/bin/python3
"""Module for serializing and deserializing data using XML."""

import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """Serializes a Python dictionary to an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the output XML file.
    """
    root = ET.Element('data')
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Deserializes an XML file to a Python dictionary.

    Args:
        filename (str): The name of the input XML file.

    Returns:
        dict: The deserialized dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        
        dictionary = {}
        for child in root:
            # Attempt to convert text back to a more specific type
            text = child.text
            try:
                # Try converting to integer
                value = int(text)
            except (ValueError, TypeError):
                try:
                    # Try converting to float
                    value = float(text)
                except (ValueError, TypeError):
                    # Handle boolean strings
                    if text.lower() == 'true':
                        value = True
                    elif text.lower() == 'false':
                        value = False
                    else:
                        # Keep as string if all conversions fail
                        value = text
            
            dictionary[child.tag] = value
            
        return dictionary
    except (FileNotFoundError, ET.ParseError):
        return None
    