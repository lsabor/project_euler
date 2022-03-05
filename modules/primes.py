# This module holds basic prime-related functions

import sequences

from tokenize import Number
from collections import Counter


P = sequences.Primes()

def is_prime(n: int) -> bool:
    # returns if n is a prime
    if n-int(n) != 0 or n < 2:
        return False
    return n in P.take_while_le(2*n)

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
    return next(p for p in P if p > n)

def prime_factorization(n: int) -> list:
    # returns the prime factorization of an int
    # e.g. 28 -> [2,2,7]
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
        n *= p**pf_counter[p]
    return n

def lcm_pf(*args: int) -> Counter:
    # returns the lcm as a prime factorization from a set of ints
    counters = map(prime_factorization,args)
    lcm_pf_counter = Counter()
    for c in counters:
        lcm_pf_counter |= c
    return lcm_pf_counter

def lcm(*args: int) -> int:
    # returns the lcm as an int from a set of ints
    return num_from_pf_counter(lcm_pf(*args))

def gcf_pf(*args: int) -> Counter:
    # returns the gcf as a prime factorization from a set of ints
    counters = list(map(prime_factorization,args))
    gcf_pf_counter = Counter()
    for c in counters:
        gcf_pf_counter |= c
    for c in counters:
        gcf_pf_counter &= c
    return gcf_pf_counter

def gcf(*args: int) -> int:
    # returns the gcf as an int from a set of ints
    return num_from_pf_counter(gcf_pf(*args))


