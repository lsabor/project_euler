# This module holds basic prime-related functions

from itertools import product

from collections import Counter
from maths.math import sqrt, iterableProduct
from maths.sequences import PrimesSeq
from maths.sets import isPrime


P = PrimesSeq()  # instantiate here so as not to reinstantiate each time
# a primeFactorization is called


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


def numFromCounter(pf_counter: Counter) -> int:
    """returns the number given a prime factorization
    doesn't check if counter is a proper prime factorization"""
    n = 1
    for p in pf_counter:
        n *= int(p) ** pf_counter[p]
    return n


def smartPFCounter(n, PF=None) -> Counter:
    """provides a hook for efficient PF generation"""
    # PF = PF if PF else Prime_Factorizations()
    # if len(PF) >= n:
    # return PF[n]
    return primeFactorization(n)


def totient(n: int) -> int:
    """counts all ints < n which are relatively prime to n"""
    factors = primeFactorization(n)
    count = n
    for p in factors:
        count *= 1 - (1 / p)
    return int(count)


def lcmPF(*args: int, PF=None) -> Counter:
    # returns the lcm as a prime factorization from a set of ints
    counters = [smartPFCounter(n, PF=PF) for n in args]
    lcmPFCounter = Counter()
    for c in counters:
        lcmPFCounter |= c
    return lcmPFCounter


def lcm(*args: int, PF=None) -> int:
    # returns the lcm as an int from a set of ints
    return numFromCounter(lcmPF(*args, PF=PF))


def gcfPF(*args: int, PF=None) -> Counter:
    # returns the gcf as a prime factorization from a set of ints
    counters = [smartPFCounter(n, PF=PF) for n in args]
    gcf_pf_counter = Counter()
    for c in counters:
        gcf_pf_counter |= c
    for c in counters:
        gcf_pf_counter &= c
    return gcf_pf_counter


def gcf(*args: int, PF=None) -> int:
    # returns the gcf as an int from a set of ints
    return numFromCounter(gcfPF(*args, PF=PF))


def divisorCountFromPFCounter(pf: Counter) -> int:
    # returns a count of all the divisors from a prime factorization
    prod = iterableProduct(map(lambda x: x + 1, pf.values()))
    return prod


def divisorCount(n: int) -> int:
    # returns a count of all the divisors of an integer
    pf = smartPFCounter(n)
    return divisorCountFromPFCounter(pf)


def divisorsFromPFCounter(pf: Counter) -> list:
    if pf == Counter():
        return [1]

    divs = []
    keys = list(pf.keys())
    values = pf.values()
    for factors in product(*[range(n + 1) for n in values]):
        div = 1
        for i, factor in enumerate(factors):
            div *= int(keys[i]) ** factor
        divs.append(div)
    return sorted(divs)


def divisors(n: int) -> list:
    # returns all the divisors of an integer
    if n <= 1:  # really, if n = 0, divisors = all natural numbers
        return [1]
    pf = smartPFCounter(n)
    return divisorsFromPFCounter(pf)


def properDivisors(n: int) -> list:
    # returns divisors of n not including n
    return divisors(n)[:-1]


def areRelativePrimes(n: int, m: int) -> bool:
    """n and m are relatively prime if their gcf is 1"""
    return gcf(n, m) == 1
