#!/usr/bin/python3
"""Module that defines a VerboseList class with verbose operations."""
from typing import SupportsIndex


class VerboseList(list):
    """List subclass that prints messages for operations."""

    def append(self, item):
        """Adds an item to the list with a message."""
        super().append(item)
        print("Added {} to the list.".format(item))

    def extend(self, x):
        """Extends the list with multiple items and prints a message."""
        super().extend(x)
        print("Extended the list with {} items.".format(len(x)))

    def remove(self, item):
        """Removes an item from the list with a message."""
        print("Removed {} from the list.".format(item))
        super().remove(item)

    def pop(self, index: SupportsIndex = -1):
        """Removes and returns an item at given index with a message."""
        item = super().pop(index)
        print("Popped {} from the list.".format(item))
        return item
