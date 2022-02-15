'''
Created on Jan 25, 2022

@author: inot
'''

import numpy as np


class NotIntegerError(ValueError):
    pass


class MatrixDimensionsError(ValueError):
    pass


def karatsuba(x, y):
    """Karatsuba algorithm for integer multiplication."""
    if not isinstance(x, int) or not isinstance(y, int):
        raise NotIntegerError('Input values must be integers.')
    if x < 10 or y < 10:
        return x * y
    no_digits = min(len(str(x)), len(str(y)))
    if no_digits % 2 == 0:
        n = int(no_digits / 2)
    else:
        n = int(no_digits / 2 + 1)
    a = x // 10 ** n
    b = x % 10 ** n
    c = y // 10 ** n
    d = y % 10 ** n
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba(a + b, c + d) - bd - ac
    return ac * 10 ** (2 * n) + ad_bc * 10 ** n + bd


def strassen(x, y):
    """Strassen's matrix multiplication algorithm.

    Regarding running time, inferior to the Coppersmith–Winograd algorithm.
    Works for square matrices with dimensions 2^n x 2^n.
    Inputs:
    x -- matrix
    y -- matrix
    returns: matrix product of x and y

    ToDo: Extend the implementation to work for matrices that AREN'T 2^n x 2^n.
    If you have a non-square non 2^n x 2^n, you can create it by adding zeros.
    """
    if len(x[0]) != len(y):
        raise MatrixDimensionsError(
            'First matrix number of columns must match second matrix number '
            'of rows.')

    if len(x) == 1 or len(y) == 1:
        return x * y

    nx = len(x) // 2
    mx = len(x) // 2
    ny = len(y) // 2
    my = len(y) // 2

    A = x[:nx][:, :mx]
    B = x[:nx][:, mx:]
    C = x[nx:][:, :mx]
    D = x[nx:][:, mx:]
    E = y[:ny][:, :my]
    F = y[:ny][:, my:]
    G = y[ny:][:, :my]
    H = y[ny:][:, my:]

    P1 = strassen(A, F - H)
    P2 = strassen(A + B, H)
    P3 = strassen(C + D, E)
    P4 = strassen(D, G - E)
    P5 = strassen(A + D, E + H)
    P6 = strassen(B - D, G + H)
    P7 = strassen(A - C, E + F)

    z11 = P5 + P4 - P2 + P6
    z12 = P1 + P2
    z21 = P3 + P4
    z22 = P1 + P5 - P3 - P7

    z = np.vstack((np.hstack((z11, z12)), np.hstack((z21, z22))))
    return z


def merge_sort_min(a):
    """
    Input:
    a -- unsorted array of n numbers
    returns: same array, sorted
    """
    if len(a) <= 1:
        return a

    sorted_output = []
    while len(a) > 0:
        sorted_output.append(min(a))
        a.remove(min(a))

    return sorted_output


def merge_sort_min_recursive(a):
    """
    Input:
    a -- unsorted array of n numbers
    returns: same array, sorted

    This algorithm recursively splits the array in half and finds the lowest
    element in each subarray with the min() function. It merges the sorted
    arrays by copying over and populating the output array in sorted order.
    """
    if len(a) <= 1:
        return a
    if len(a) % 2 == 0:
        n = int(len(a) / 2)
    else:
        n = int(len(a) / 2 + 1)
    left_array = a[:n]
    right_array = a[n:]
    left_half = merge_sort_recursive(left_array)
    right_half = merge_sort_recursive(right_array)

    sorted_output = []
    while len(left_half) + len(right_half) > 0:
        if len(left_half) == 0 or len(right_half) == 0:
            if len(left_half) == 0:
                sorted_output.append(min(right_half))
                right_half.remove(min(right_half))
            else:
                sorted_output.append(min(left_half))
                left_half.remove(min(left_half))
            continue
        left_min = min(left_half)
        right_min = min(right_half)
        if left_min <= right_min:
            sorted_output.append(left_min)
            left_half.remove(left_min)
        else:
            sorted_output.append(right_min)
            right_half.remove(right_min)

    return sorted_output


def merge_sort_recursive(a):
    """Merge sort algorithm is a standard sorting algorithm with O(n*log(n)).

    Input:
    a -- unsorted array of n numbers
    returns: same array, sorted

    This algorithm splits the array in half and copies those halves into two
    new arrays. Then it solves both halves recursively and combines the
    results. It merges the sorted arrays by copying over and populating the
    output array in sorted order. It accounts for arrays with duplicates and
    with only distinct elements. Uses less or equal when comparing minimum
    values in left_half and righ_half to ensure that the duplicate from
    left_half is appended to sorted_output first. This is crucial for
    count_inversions to work as intended when it uses this subroutine. Empty
    array and array of length=1 are actually the basic recursion case.
    Recursion sort is faster than min sort! Compared to the RealPython
    implmentation, it is still slightly slower.
    """
    if len(a) <= 1:
        return a
    if len(a) % 2 == 0:
        n = int(len(a) / 2)
    else:
        n = int(len(a) / 2 + 1)
    left_array = a[:n]
    right_array = a[n:]
    left_half = merge_sort_recursive(left_array)
    right_half = merge_sort_recursive(right_array)

    sorted_output = []
    left_index = right_index = 0
    while len(left_half) + len(right_half) > len(sorted_output):
        if left_index == len(left_half) or right_index == len(right_half):
            if left_index == len(left_half):
                sorted_output += right_half[right_index:]
            else:
                sorted_output += left_half[left_index:]
            continue
        left_min = left_half[left_index]
        right_min = right_half[right_index]
        if left_min <= right_min:
            sorted_output.append(left_min)
            left_index += 1
        else:
            sorted_output.append(right_min)
            right_index += 1

    return sorted_output


def merge_sort_real_python(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array
    midpoint = len(array) // 2
    # Sort the array by recursively splitting the input
    # into two equal halves, sorting each half and merging them
    # together into the final result
    return merge(
        left=merge_sort_real_python(array[:midpoint]),
        right=merge_sort_real_python(array[midpoint:]))


def merge(left, right):
    # If the first array is empty, then nothing needs
    # to be merged, and you can return the second array as the result
    if len(left) == 0:
        return right
    # If the second array is empty, then nothing needs
    # to be merged, and you can return the first array as the result
    if len(right) == 0:
        return left
    result = []
    index_left = index_right = 0
    # Now go through both arrays until all the elements
    # make it into the resultant array
    while len(result) < len(left) + len(right):
        # The elements need to be sorted to add them to the
        # resultant array, so you need to decide whether to get
        # the next element from the first or the second array
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
        # If you reach the end of either array, then you can
        # add the remaining elements from the other array to
        # the result and break the loop
        if index_right == len(right):
            result += left[index_left:]
            break
        if index_left == len(left):
            result += right[index_right:]
            break
    return result


def count_inversions(A):
    """Count inversions of an array.

    Inversions are pairs of array indices (i, j) where i < j and A[i] > A[j].
    A sorted array has zero inversions.

    Input:
    a -- unsorted array of n numbers
    returns: sorted input array, number of inversions
    """
    if len(A) <= 1:
        return A, 0
    if len(A) % 2 == 0:
        n = int(len(A) / 2)
    else:
        n = int(len(A) / 2 + 1)
    left_array = A[:n]
    right_array = A[n:]
    left_half, left_inversions = count_inversions(left_array)
    right_half, right_inversions = count_inversions(right_array)

    sorted_output = []
    left_index = right_index = 0
    split_inversions = 0
    while len(left_half) + len(right_half) > len(sorted_output):
        if left_index == len(left_half) or right_index == len(right_half):
            if left_index == len(left_half):
                sorted_output += right_half[right_index:]
            else:
                sorted_output += left_half[left_index:]
            continue
        left_min = left_half[left_index]
        right_min = right_half[right_index]
        if left_min <= right_min:
            sorted_output.append(left_min)
            left_index += 1
        else:
            sorted_output.append(right_min)
            right_index += 1
            split_inversions += len(left_half) - left_index

    return sorted_output, left_inversions + right_inversions + split_inversions
