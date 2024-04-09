#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class MaxIntegerTest(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_max(self):
        """Test for max in list of integera"""
        self.assertEqual(max_integer([1, 3, 5, 7, 5]), 7)

    def test_float(self):
        """Test for max in list of floats"""
        self.assertEqual(max_integer([3.0, 2.2, 3.2, 1.0, 2]), 3.2)

    def test_int_float(self):
        """Test for max in list of int and float"""
        self.assertEqual(max_integer([3, 5.2, 8.2, 8, 6]), 8.2)

    def test_ordered_list(self):
        """Test for max in an ordered list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_unordered_list(self):
        """Test for max in an unordered list of integers."""
        self.assertEqual(max_integer([6, 1, 7, 3, 4]), 7)

    def test_empty(self):
        """Function should return None if the list is empty"""
        self.assertEqual(max_integer([]), None)

    def test_negative_int(self):
        """Test for max with negative int"""
        self.assertEqual(max_integer([3, -3, 5, -9, -12, 12, 4]), 12)

    def test_string(self):
        """Test a string."""
        string = "Brennan"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
