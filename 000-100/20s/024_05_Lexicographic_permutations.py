"""
## Lexicographic permutations
Problem 24

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


Link: https://projecteuler.net/problem=24

Date solved:  
2022/04/02
"""

# TODO: refactor for speed


ANSWER = 2783915460

# imports

from maths.math import permutations

# solution


def solution(bypass=False):
    if bypass:
        return ANSWER
    ls = list(range(10))

    perms = list(permutations(ls))
    perms.sort()

    millionth = perms[int(1e6 - 1)]
    result = 0
    for i, val in enumerate(millionth):
        result += val * 10 ** (len(millionth) - i - 1)

    return result


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution(bypass=False)
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
