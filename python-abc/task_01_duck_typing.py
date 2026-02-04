#!/usr/bin/python3
"""Module that demonstrates duck typing with shapes"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract base class for shapes"""
    
    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape"""
        pass


class Circle(Shape):
    """Circle class that inherits from Shape"""
    
    def __init__(self, radius):
        """Initialize a circle with radius
        
        Args:
            radius: radius of the circle
        """
        self.radius = abs(radius)

    def area(self):
        """Calculate and return the area of the circle"""
        return pi * (self.radius ** 2)
    
    def perimeter(self):
        """Calculate and return the perimeter of the circle"""
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Rectangle class that inherits from Shape"""
    
    def __init__(self, width, height):
        """Initialize a rectangle with width and height
        
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height

    def area(self):
        """Calculate and return the area of the rectangle"""
        return self.width * self.height
    
    def perimeter(self):
        """Calculate and return the perimeter of the rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter of a shape
    
    Args:
        shape: any object that has area() and perimeter() methods
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
