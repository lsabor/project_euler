"""
## Distinct primes factors
Problem 47

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?



Link: https://projecteuler.net/problem=47

Date solved:  
2022/07/24
"""

ANSWER = 134043

# imports

from maths.sequences.compound import PrimeFactorSeq
from maths.primes import numFromCounter

# solution

pfs = PrimeFactorSeq()  # TODO: deserialize/serialize very inefficient


def find_consecutive_pf_counts(n):
    count = 0
    current = 0

    i = 0
    for pf in pfs:  # TODO: cache shouldn't rewrite for every single item
        if len(pf) == n:
            if count == 0:
                current = numFromCounter(pf)
            count += 1
            if count == n:
                return current
        else:
            count = 0


def solution():

    return find_consecutive_pf_counts(4)


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution()
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
