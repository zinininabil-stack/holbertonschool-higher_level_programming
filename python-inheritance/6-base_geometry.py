#!/usr/bin/python3
"""Module that defines BaseGeometry class"""


class BaseGeometry:
    """A base class for geometry operations"""
    
    def area(self):
        """Raises an exception indicating area() is not implemented"""
        raise Exception("area() is not implemented")
