# This module holds basic prime-related functions

import sequences

from tokenize import Number
from collections import Counter


P = sequences.Primes()

def is_prime(n: int) -> bool:
    # returns if n is a prime
    if n-int(n) != 0 or n < 2:
        return False
    return n == P.take_while_le(n)[-1]

def prev_prime(n: Number) -> int:
    # returns the next prime smaller than n, None if n <= 2
    if n <= 2:
        return None
    if is_prime(n):
        n = n-1
    return P.take_while_lt(n)[-1]

def next_prime(n: Number) -> int:
    # returns the next prime larger than n
    if n < 2:
        return 2
    return next(p for p in P.take_while_le(2*n) if p > n)

def prime_factorization(n: int) -> Counter:
    # returns the prime factorization of an int
    # e.g. 28 -> Counter({2:2,7:1})
    if n - int(n) != 0:
        raise Exception(f'cannot prime factorize {n} - not a whole number')
    factors = []
    p = 2
    while n != 1:
        while n%p == 0:
            factors.append(p)
            n = n//p
        p = next_prime(p)
    return Counter(factors)

def num_from_pf_counter(pf_counter: Counter) -> int:
    # returns the number given a prime factorization
    # doesn't check if counter is a proper prime factorization
    n = 1
    for p in pf_counter:
        n *= int(p)**pf_counter[p]
    return n




