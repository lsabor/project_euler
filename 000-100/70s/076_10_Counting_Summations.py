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
from maths.sequences.special_sequences import PentagonalNumbers

# solution


PN = PentagonalNumbers()


@lru_cache(100)
def p(n):
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
        result += sign * p(next_value)
        if next_value < delta:
            break
        result += sign * p(next_value - delta)

        i += 1
        delta += 1
        sign *= -1
    return result


def solution(bypass=True):
    if bypass:
        return ANSWER

    return p(100) - 1


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution(bypass=False)
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
