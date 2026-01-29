#!/usr/bin/python3
"""Module that defines a Square class"""


class Square:
    """Class that defines a square with private size attribute and validation"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size * self.__size

    @property
    def size(self):
        """ Privante instance method that returns the current size"""
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def my_print(self):
        """ Function printing square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):  #Rows
                for j in range(self.__size):  # Columns
                    print("#", end="")
                print() 
