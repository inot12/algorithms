'''
Created on Jan 27, 2022

@author: inot
'''

import cProfile
import random as rn
import timeit as ti

import algorithms as alg


def main():
    a = [int(1000 * rn.random()) for _ in range(10000)]

    start = ti.default_timer()
    alg.merge_sort_min(a)
    print("Merge sort execution time:", ti.default_timer() - start)
    cProfile.run(f"alg.merge_sort_min({a})")

    start = ti.default_timer()
    alg.merge_sort_real_python(a)
    print("Merge sort execution time:", ti.default_timer() - start)
    cProfile.run(f"alg.merge_sort_real_python({a})")

    start = ti.default_timer()
    alg.merge_sort_recursive(a)
    print("Merge sort execution time:", ti.default_timer() - start)
    cProfile.run(f"alg.merge_sort_recursive({a})")


if __name__ == "__main__":
    main()
