"""
Counting summations
Problem 76

It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?

Link: https://projecteuler.net/problem=76

Date solved:  
2022/09/08
Solved with DeMehr Haywood
"""

# TODO: refactor for speed

ANSWER = 190569291

# imports

from functools import lru_cache

# solution


# @lru_cache
# def H(n, a):
#     if a == 1 or n == a:
#         print(n, a, 1)
#         return 1
#     if a > n:
#         print(n, a, 0)
#         return 0

#     end = min(a, n - a)

#     result = sum([H(n - a, b) for b in range(1, end + 1)])

#     print(n, a, result)

#     return result


# def f(n):
#     return sum([H(n, a) for a in range(1, n + 1)])


# n = 100
# M = [[0] * n for _ in range(n)]
# for k in range(n):
#     M[k][k] = 1
#     i = k
#     while i > 0:
#         M[k][k - i] = sum(M[i - 1][k - i :])
#         i -= 1

history = [[]]


def count_partitions(n, history):
    """returns a list which represents the count of all partitionings of n where {index+1} is
    exactly equal to the smallest partition in the partitioning of n
    e.g.
    n = 1 -> [1]
    n = 2 -> [1, 1]
    n = 3 -> [2, 0, 1]
    n = 4 -> [3, 1, 0, 1]
    n = 5 -> [5, 1, 0, 0, 1]

    notice:
    1. result[len(n)-1] == 1
    2. result[m] == sum(history[-m][m-1:]) (when len(history[-m]) >= m)
    """
    result = []
    for m in range(n):
        if m == n:
            value = 1
        elif m >= n/2:
            value = 0
        else:
            value = sum(history[-m][])




def solution(bypass=True):
    if bypass:
        return ANSWER

    return sum(M[-1]) - 1


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution(bypass=False)
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
