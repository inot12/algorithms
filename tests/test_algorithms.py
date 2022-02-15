#! /home/inot/.pyenv/shims/python3
"""
Created on Jan 26, 2022

@author: inot
"""

import unittest

import numpy as np

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

    def test_bad_input(self):
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


class StrassenGoodInput(unittest.TestCase):
    """Test for good input of function strassen()."""

    def setUp(self):
        # Current implementation does not work for non 2^n x 2^n matrices.
        # Non 2^n x 2^n matrix does not work.
        # self.x = np.array([[2, 5, 8, 2],
        #                    [1, 9, 3, 3],
        #                    [6, 7, 9, 0],
        #                    [1, 9, 6, 7],
        #                    [4, 3, 7, 8]])
        # self.y = np.array([[1, 8, 7],
        #                    [9, 8, 5],
        #                    [6, 2, 3],
        #                    [7, 9, 4]])
        # self.z = np.array([[109, 90, 71],
        #                    [121, 113, 73],
        #                    [123, 122, 104],
        #                    [167, 155, 98],
        #                    [129, 142, 96]])

        # 2^n x 2^n matrix works.
        self.x = np.array([[2, 5, 8, 2],
                           [1, 9, 3, 3],
                           [6, 7, 9, 0],
                           [4, 3, 7, 8]])
        self.y = np.array([[1, 8, 7, 5],
                           [9, 8, 5, 2],
                           [6, 2, 3, 7],
                           [7, 9, 4, 1]])
        self.z = np.array([[109, 90, 71, 78],
                           [121, 113, 73, 47],
                           [123, 122, 104, 107],
                           [129, 142, 96, 83]])

    def test_general_case(self):
        """strassen() should return known results for known values."""
        self.assertTrue(np.allclose(alg.strassen(self.x, self.y), self.z))


class StrassenBadInput(unittest.TestCase):
    """Test for bad input of function strassen()."""

    def setUp(self):
        self.x = np.random.rand(3, 4)
        self.y = np.random.rand(5, 2)

    def test_bad_input(self):
        """strassen() should fail if matrix dimensons don't match."""
        self.assertRaises(alg.MatrixDimensionsError, alg.strassen,
                          self.x, self.y)


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
