#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_normal_case(self):
        """Test normal case - find biggest number"""
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_empty_list(self):
        """Test empty list - should return None"""
        self.assertIsNone(max_integer([]))

    def test_one_number(self):
        """Test with only one number"""
        self.assertEqual(max_integer([5]), 5)
    
    def test_max_begenning(self):
        """Max at the begenning"""
        self.assertEqual(max_integer([3, 2, 1]), 3)

    def test_max_middle(self):
        """Max in the middle"""
        self.assertEqual(max_integer([1, 3, 1]), 3)

    def test_one_negative(self):
        """One negative number in the list"""
        self.assertEqual(max_integer([-1, 1, 2]), 2)

    def test_only_negative(self):
        """Only negative numbers in the list"""
        self.assertEqual(max_integer([-1, -2, -3]), -1)

if __name__ == '__main__':
    unittest.main()
    