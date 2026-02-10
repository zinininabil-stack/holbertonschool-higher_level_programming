#!/usr/bin/python3
""""""
import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(age, int):
            raise TypeError("age must be an integer")
        if not isinstance(is_student, bool):
            raise TypeError("is_student must be a boolean")
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")
            
    def serialize(self, filename):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
                return None
    
    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError, EOFError, AttributeError, ImportError, IndexError):
            return None

