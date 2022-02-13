#! /home/inot/.pyenv/shims/python3
"""
Created on Jan 26, 2022

@author: inot
"""

import unittest

import algorithms as alg


class KaratsubaGoodInput(unittest.TestCase):
    """Test for good input of function karatsuba()."""

    def test_general_case(self):
        """karatsuba() should return known results for known values."""
        self.assertEqual(alg.karatsuba(23718, 113), 2680134)

    # def test_case2(self):
    #     """f should return known results for known values."""
    #     self.assertAlmostEqual(f(known_value), known_result, delta=1e-5)


class KaratsubaBadInput(unittest.TestCase):
    """Test for bad input of function karatsuba()."""

    def test_case1(self):
        """karatusba() should fail if all input values are not integers."""
        self.assertRaises(alg.NotIntegerError, alg.karatsuba, 2361.7, 125)

    # def test_case2(self):
    #     """Alternative with context manager.
    #
    #     Use if you have more exceptions of the same type.
    #     """
    #     with self.assertRaises(ValueError):
    #         calc.divide(10, 0)
    #         calc.divide(10, '1')


class MergeSortMinGoodInput(unittest.TestCase):
    """Test for good input of function merge_sort_min()."""

    def test_general_case(self):
        """merge_sort_min() should return known results for known values."""
        self.assertEqual(alg.merge_sort_min([7, 2, 4, 5, 3, 4, 8, 1, 5]),
                         [1, 2, 3, 4, 4, 5, 5, 7, 8])
        self.assertEqual(alg.merge_sort_min([]), [])
        self.assertEqual(alg.merge_sort_min([12]), [12])


class MergeSortMinRecursiveGoodInput(unittest.TestCase):
    """Test for good input of function merge_sort_min_recursive()."""

    def test_general_case(self):
        """merge_sort_min_recursive() should return known results for known
        values."""
        self.assertEqual(alg.merge_sort_min_recursive(
            [7, 2, 4, 5, 3, 4, 8, 1, 5]),
            [1, 2, 3, 4, 4, 5, 5, 7, 8])
        self.assertEqual(alg.merge_sort_min_recursive([]), [])
        self.assertEqual(alg.merge_sort_min_recursive([12]), [12])


class MergeSortRecursiveGoodInput(unittest.TestCase):
    """Test for good input of function merge_sort_recursive()."""

    def test_general_case(self):
        """merge_sort_recursive() should return known results for known
        values."""
        self.assertEqual(alg.merge_sort_recursive([7, 2, 4, 5, 3, 4, 8, 1, 5]),
                         [1, 2, 3, 4, 4, 5, 5, 7, 8])
        self.assertEqual(alg.merge_sort_recursive([]), [])
        self.assertEqual(alg.merge_sort_recursive([12]), [12])


class CountInversionsGoodInput(unittest.TestCase):
    """Test for good input of function count_inversions()."""

    def test_general_case(self):
        """count_inversions() should return known results for known values."""
        self.assertEqual(alg.count_inversions([7, 2, 4, 5, 3, 4, 8, 1, 5]),
                         ([1, 2, 3, 4, 4, 5, 5, 7, 8], 17))
        self.assertEqual(alg.count_inversions([]), ([], 0))
        self.assertEqual(alg.count_inversions([12]), ([12], 0))


def main():
    unittest.main(verbosity=2)


if __name__ == "__main__":
    main()
