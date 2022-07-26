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


def is_prime_single_check_old(n: int) -> bool:
    """returns if n is a prime, but doesn't update the Primes sequence"""
    # to check if n is prime, we only have to check if
    # it's divisible by any primes less than the square root of it
    if P[-1] < sqrt(n):
        raise ValueError(
            f"n is too large for this method. Keep it under {P[-1]**2}, or extend Primes seq"
        )
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


def is_prime_single_check(n: int) -> bool:
    """uses Miller-Rabin primality test
    only effective up to 3,317,044,064,679,887,385,961,981"""
    if n % 2 == 0:
        return False
    if n < 2047:
        bases = [2]
    elif n < 1373653:
        bases = [2, 3]
    elif n < 9080191:
        bases = [31, 73]
    elif n < 25326001:
        bases = [2, 3, 5]
    elif n < 3215031751:
        bases = [2, 3, 5, 7]
    elif n < 4759123141:
        bases = [2, 7, 61]
    elif n < 1122004669633:
        bases = [2, 13, 23, 1662803]
    elif n < 2152302898747:
        bases = [2, 3, 5, 7, 11]
    elif n < 3474749660383:
        bases = [2, 3, 5, 7, 11, 13]
    elif n < 341550071728321:
        bases = [2, 3, 5, 7, 11, 13, 17]
    elif n < 3825123056546413051:
        bases = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    elif n < 318665857834031151167461:
        bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    elif n < 3317044064679887385961981:
        bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    else:
        raise ValueError("n too big to handle with this test")

    # get n in the form n = 2^s * d + 1 where d is odd
    s = 0
    d = n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    from maths import modex

    # Testing
    for a in bases:
        passes = False
        if modex(a, d, n) == 1:
            passes = True
        for r in range(s):
            if modex(a, (2**r) * d, n) == n - 1:
                passes = True
        if not passes:
            return False
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
        if (p >= sqrt(n)) or (p == n):
            factors.append(n)
            n = 1
        while n % p == 0:
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
