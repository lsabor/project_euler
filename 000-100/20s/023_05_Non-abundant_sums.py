"""
## Non-abundant sums

Problem 23

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

Link: https://projecteuler.net/problem=23

Date solved:  
2022/04/02
"""

# TODO: refactor for speed

ANSWER = 4179871

# imports

from maths.sequences.compound import DivisorSeq, PrimeFactorSeq
from maths.math import product

# solution

PFS = PrimeFactorSeq()
DS = DivisorSeq()

search_depth = 28124
PFS[search_depth]  # make sure PFS is populated up to search_depth, makes next step easier
DS[search_depth]  # make sure DS is populated up to search_depth


def get_abundant_numbers(search_depth):
    abundant_numbers = []
    for n in range(2, search_depth):
        if n < (sum(DS.seq[n]) - n):
            abundant_numbers.append(n)
    return abundant_numbers


def sumNonAbundants(seach_depth):
    abundant_numbers = get_abundant_numbers(search_depth)

    not_sum_of_two_abundants = set(range(search_depth))
    for i, j in product(abundant_numbers, abundant_numbers):
        s = i + j
        if s in not_sum_of_two_abundants:
            not_sum_of_two_abundants.remove(s)

    return sum(not_sum_of_two_abundants)


def solution(bypass=False):
    if bypass:
        return ANSWER
    return sumNonAbundants(search_depth)


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution(bypass=False)
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer =", ANSWER)
