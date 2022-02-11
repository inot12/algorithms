'''
Created on Jan 25, 2022

@author: inot
'''


class NotIntegerError(ValueError):
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


def merge_sort_min(a):
    """Merge sort algorithm is a standard sorting algorithm.

    Input:
    a -- unsorted array of n numbers
    returns: same array, sorted

    This algorithm splits the array in half and copies those halves into two
    new arrays. Then it finds the lowest element in each array with the min()
    function. It merges the sorted arrays by copying over and populating the
    output array in sorted order. It accounts for arrays with duplicates and
    with only distinct elements. min() is slower than recursion!
    Empty array and array of length=1 are actually the basic recursion case.
    """
    if len(a) <= 1:
        return a
    if len(a) % 2 == 0:
        n = int(len(a) / 2)
    else:
        n = int(len(a) / 2 + 1)
    left_array = a[:n]
    right_array = a[n:]

    sorted_output = []
    while len(left_array) + len(right_array) > 0:
        if len(left_array) == 0 or len(right_array) == 0:
            if len(left_array) == 0:
                sorted_output.append(min(right_array))
                right_array.remove(min(right_array))
            else:
                sorted_output.append(min(left_array))
                left_array.remove(min(left_array))
            continue
        left_min = min(left_array)
        right_min = min(right_array)
        if left_min < right_min:
            sorted_output.append(left_min)
            left_array.remove(left_min)
        else:
            sorted_output.append(right_min)
            right_array.remove(right_min)

    return sorted_output


def merge_sort_recursive(a):
    """Merge sort algorithm is a standard sorting algorithm.

    Input:
    a -- unsorted array of n numbers
    returns: same array, sorted

    This algorithm splits the array in half and copies those halves into two
    new arrays. Then it solves both halves recursively and combines the
    results. It merges the sorted arrays by copying over and populating the
    output array in sorted order. It accounts for arrays with duplicates and
    with only distinct elements. Recursion sorting is faster!
    Empty array and array of length=1 are actually the basic recursion case.
    Compared to the RealPython implmentation, it is still slightly slower.
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
        if len(left_half) == left_index or len(right_half) == right_index:
            if len(left_half) == left_index:
                sorted_output += right_half[right_index:]
            else:
                sorted_output += left_half[left_index:]
            continue
        left_min = left_half[left_index]
        right_min = right_half[right_index]
        if left_min < right_min:
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
