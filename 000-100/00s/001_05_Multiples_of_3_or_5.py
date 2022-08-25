"""
## Multiples of 3 or 5
Problem 1

Problem statement:  
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Link: https://projecteuler.net/problem=1

Date solved:  
2022/03/05
"""

ANSWER = 233168

# imports

from maths.primes import lcm
from maths.math import sumConsecutiveInts


# solution


def solution(bypass=False):
    if bypass:
        return ANSWER
    max_val = 1000

    mults_3 = set(range(max_val)[::3])
    mults_5 = set(range(max_val)[::5])

    mults_3_or_5 = mults_3.union(mults_5)

    return sum(mults_3_or_5)


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution(bypass=False)
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer =", ANSWER)
