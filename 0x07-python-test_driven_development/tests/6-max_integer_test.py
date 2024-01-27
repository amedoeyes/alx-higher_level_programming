#!/usr/bin/python3

"""Unittest for max_integer([..])"""

import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Defines unit tests for max_integer.py"""

    def test_empty_list(self):
        """Tests an empty list"""
        self.assertIsNone(max_integer([]), None)

    def test_one_element(self):
        """Tests a list with one element"""
        self.assertEqual(max_integer([1]), 1)

    def test_max_at_start(self):
        """Tests a list with the max at the start"""
        self.assertEqual(max_integer([2, 1, 5, 3, 4]), 5)

    def test_max_at_end(self):
        """Tests a list with the max at the end"""
        self.assertEqual(max_integer([1, 5, 3, 4, 2]), 5)

    def test_max_in_middle(self):
        """Tests a list with the max in the middle"""
        self.assertEqual(max_integer([1, 3, 5, 4, 2]), 5)

    def test_all_same(self):
        """Tests a list with all the same elements"""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_negative(self):
        """Tests a list with negative elements"""
        self.assertEqual(max_integer([-5, 5, 1, 2]), 5)

    def test_all_negative(self):
        """Tests a list with all negative elements"""
        self.assertEqual(max_integer([-5, -5, -5, -5]), -5)

    def test_floats(self):
        """Tests a list with floats"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 4.5]), 4.5)

    def test_mixed(self):
        """Tests a mixed list"""
        self.assertEqual(max_integer([1, 2.5, 3, 4.5]), 4.5)

    def test_empty_string(self):
        """Tests an empty string"""
        self.assertIsNone(max_integer(""), None)

    def test_string(self):
        """Tests a list with strings"""
        self.assertEqual(max_integer(["a", "b", "c"]), "c")


if __name__ == "__main__":
    unittest.main()
