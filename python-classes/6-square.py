#!/usr/bin/python3
"""Module that defines a Square class"""


class Square:
    """Class that defines a square with private size and position attributes"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position with validation"""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square with the character # at given position"""
        if self.__size == 0:
            print()
            return

        # Print vertical offset (position[1])
        for i in range(self.__position[1]):
            print()

        # Print the square with horizontal offset (position[0])
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
