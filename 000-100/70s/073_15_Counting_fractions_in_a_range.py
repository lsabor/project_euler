"""
## Counting fractions in a range
Problem 73

Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?

Link: https://projecteuler.net/problem=73

Date solved:  
2022/08/17
"""

# TODO: refactor for speed

ANSWER = 7295372

# imports

from maths.math import ceil
from maths.sequences.compound import PrimeFactorSeq

# solution

# for each denominator <= 12e3, we'll search through the range of n's between
# d/3 and d/2 exclusive
# Then increment our count on if n & d share no factors.
# this can easily be done with the precalculated Prime Factorizations (PrimeFactorSeq)

threshold = int(12e3)


def closest_ordered_fraction(threshold):
    pfs = PrimeFactorSeq()[: threshold + 1]

    lower_bound = 1 / 3
    upper_bound = 1 / 2
    count = 0

    for d, pf in enumerate(pfs):
        if d == 0:
            continue
        d_factors = set(pf)

        lower_n = ceil(lower_bound * d)
        lower_n += lower_n / d == lower_bound
        upper_n = int(upper_bound * d)
        upper_n -= upper_n / d == upper_bound

        for n in range(lower_n, upper_n + 1):
            if d == n:
                continue
            n_factors = set(pfs[n])
            # only inc count if d and n are relatively prime (share no factors)
            count += not bool(d_factors.intersection(n_factors))

    return count


def solution(bypass=False):
    if bypass:
        return ANSWER

    return closest_ordered_fraction(threshold)


if __name__ == "__main__":
    solution(bypass=False)
