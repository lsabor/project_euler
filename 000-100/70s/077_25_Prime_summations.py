"""
Prime summations
Problem 77

It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five thousand different ways?

Link: https://projecteuler.net/problem=77

Date solved:
09/10/2022  
"""


ANSWER = 71

# imports

from functools import lru_cache

from maths.sequences.special_sequences import PrimesSeq

# solution


primes = PrimesSeq().seq


@lru_cache(100)
def H(n, a):
    if a == n:
        return 1
    if a == 1:
        return not n % 2
    if a > n:
        return 0

    summation = 0
    i = 0
    p = primes[i]
    while p <= a and p <= n - a:
        summation += H(n - a, p)
        i += 1
        p = primes[i]

    return summation


def f(n):

    summation = 0
    i = 0
    p = primes[i]
    while p <= n:
        summation += H(n, p)
        i += 1
        p = primes[i]

    return summation


def solution(bypass=False):
    if bypass:
        return ANSWER

    threshold = 5000

    n = 2
    while True:
        if f(n) > threshold:
            return n
        n += 1


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution(bypass=False)
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
