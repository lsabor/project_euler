"""
Coin partitions

Problem 78

Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.
OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O

Find the least value of n for which p(n) is divisible by one million.


Link: https://projecteuler.net/problem=78

Date solved:  
"""

ANSWER = 0

# imports

from functools import lru_cache

# solution


# @lru_cache
def H(n, a, m):
    if a == 1 or n == a:
        return 1
    if a > n:
        return 0

    return sum([H(n - a, b, m) for b in range(1, a + 1)]) % m


def f(n, m):
    return sum([H(n, a, m) for a in range(1, n + 1)]) % m


def solution(bypass=True):
    if bypass:
        return ANSWER

    modulo = 1000

    n = 1
    while True:
        fnm = f(n, modulo)
        print(n, fnm)
        if fnm == 0:
            return n
        n += 1


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution(bypass=False)
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
