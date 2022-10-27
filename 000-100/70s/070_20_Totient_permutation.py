"""
## Totient permutation

Problem 70

Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 1e7, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.


Link: https://projecteuler.net/problem=70

Date solved:  
2022/08/13  
solved with Michael Morgan  
"""

ANSWER = 8319823

# imports

from maths.math import combinations
from maths.sequences import PrimesSeq

# solution

# since n/phi(n) is minimized when n has fewest factors
# if n is prime, phi(n) is n-1, and thus not a permutation of n
# so we look for n that is composite, with fewest factors.
# We can choose 2 prime numbers from near sqrt(1e7)
# 1e4 > sqrt(1e7), so we'll search through pairs of primes all lower than 1e4

P = PrimesSeq()
Ps = P.takeWhileLT(1e4)


def is_permutation(a: int, b: int) -> bool:
    return sorted(str(a)) == sorted(str(b))


def prod_totient(p1, p2) -> tuple[int, int]:
    """returns the totient of p1*p2 given p1 and p2 are prime"""
    prod = p1 * p2
    totient = prod - p1 - p2 + 1
    return prod, totient


def totient_permutation():
    answers = []

    for p1, p2 in combinations(Ps, 2):
        n, totient = prod_totient(p1, p2)
        if n >= 10**7:
            continue
        if is_permutation(n, totient):
            ratio = n / totient
            answers.append((ratio, n, totient, (p1, p2)))

    return sorted(answers)[0]


def solution():

    return totient_permutation()[1]


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution()
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
