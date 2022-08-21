# This module holds basic prime-related functions


from collections import Counter
from math import sqrt
from maths.sequences import PrimesSeq
from maths.sets import isPrime

P = PrimesSeq()  # instantiate here so as not to reinstantiate each time
# a primeFactorization is called


# def prev_prime(n) -> int:
#     """returns the next prime smaller than n, None if n <= 2"""
#     if n <= 2:
#         return None
#     if isPrime(n):
#         n = n - 1
#     return P.take_while_lt(n)[-1]


# def next_prime(n) -> int:
#     # returns the next prime larger than n
#     if n < 2:
#         return 2
#     return next(p for p in P.take_while_le(2 * n) if p > n)


def primeFactorization(n: int) -> Counter:
    """returns the prime factorization of an int
    e.g. 28 -> Counter({2:2,7:1})"""

    if (n < 0) or (n % 1 != 0):
        raise ValueError(f"cannot prime factorize {n} - not a natural number")
    if n in (0, 1):
        return Counter()
    if n == 2:
        return Counter([2])
    factors = []
    index = 0
    while n > 1:
        p = P[index]
        if (p > sqrt(n)) or (p == n):
            factors.append(n)
            n = 1
        while n % p == 0:
            factors.append(p)
            n = n // p
        if n == 1:
            break
        index += 1
    return Counter(factors)


def numFromPFCounter(pf_counter: Counter) -> int:
    # returns the number given a prime factorization
    # doesn't check if counter is a proper prime factorization
    n = 1
    for p in pf_counter:
        n *= int(p) ** pf_counter[p]
    return n
