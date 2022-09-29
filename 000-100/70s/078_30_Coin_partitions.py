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
09/11/2022
"""

# TODO: refactor for speed

ANSWER = 55374

# imports

from functools import lru_cache
from maths.sequences.special_sequences import PentagonalNumbers

# solution


PN = PentagonalNumbers()


@lru_cache(100000)
def p(n, m):
    if n == 1 or n == 0:
        return 1
    result = 0
    i = 1
    delta = 1
    sign = 1
    while True:
        pentagonal = PN[i - 1]

        if (next_value := n - pentagonal) < 0:
            break
        result += sign * p(next_value, m)
        if next_value < delta:
            break
        result += sign * p(next_value - delta, m)

        i += 1
        delta += 1
        sign *= -1
    return result % m


def solution():

    m = 1000000

    n = 1
    count = p(n, m)
    while count % m:
        n += 1
        count = p(n, m)

    return n


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution()
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
