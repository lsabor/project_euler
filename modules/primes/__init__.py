# This module holds basic prime-related functions

import sequences

from collections import Counter
from math import sqrt


P = sequences.Primes()


def is_prime(n: int) -> bool:
    """returns if n is a prime"""
    if n - int(n) != 0 or n < 2:
        return False
    return n == P.take_while_le(n)[-1]


def is_prime_single_check(n: int) -> bool:
    """returns if n is a prime, but doesn't update the Primes sequence"""
    # to check if n is prime, we only have to check if
    # it's divisible by any primes less than the square root of it
    if (n < 1) or (n % 1 != 0):
        return False
    if n == 2:
        return True

    p = 2
    while p < sqrt(n):
        if n % p == 0:
            return False
        p = next_prime(p)
    return True


def prev_prime(n) -> int:
    """returns the next prime smaller than n, None if n <= 2"""
    if n <= 2:
        return None
    if is_prime(n):
        n = n - 1
    return P.take_while_lt(n)[-1]


def next_prime(n) -> int:
    # returns the next prime larger than n
    if n < 2:
        return 2
    return next(p for p in P.take_while_le(2 * n) if p > n)


def prime_factorization(n: int) -> Counter:
    # returns the prime factorization of an int
    # e.g. 28 -> Counter({2:2,7:1})
    if (n < 1) or (n - int(n) != 0):
        raise ValueError(f"cannot prime factorize {n} - not a positive integer")
    if n == 2:
        return Counter([2])
    factors = []
    p = 2
    while n != 1:
        while n % p == 0 and p <= sqrt(n):
            factors.append(p)
            n = n // p
        p = next_prime(p)
    return Counter(factors)


def num_from_pf_counter(pf_counter: Counter) -> int:
    # returns the number given a prime factorization
    # doesn't check if counter is a proper prime factorization
    n = 1
    for p in pf_counter:
        n *= int(p) ** pf_counter[p]
    return n
