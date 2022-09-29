"""
## Counting fractions
Problem 72

Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?

Link: https://projecteuler.net/problem=72

Date solved:  
2022/08/16
"""

# TODO: refactor for speed

ANSWER = 303963552391

# imports

from maths.sequences import PrimesSeq

# solution

# is equivalent to sum of totients from 1 -> 1e6, which sucks to compute
# we will use a seiving tactic to calculate the totients of all numbers in the range

threshold = int(1e6)
ps = PrimesSeq().takeWhileLE(threshold)


def count_unique_fractions(threshold):
    totients = list(range(2, threshold + 1))
    for p in ps:
        current = p
        ratio = 1 - 1 / p
        while current <= threshold:
            totients[current - 2] *= ratio
            current += p
    return int(sum(totients))


def solution():

    return count_unique_fractions(threshold)


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution()
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
