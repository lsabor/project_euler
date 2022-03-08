# This module holds basic math functions

import primes
from collections import Counter

def sum_consecutive_ints(n: int) -> int:
    # returns sum of consecutive ints up to and including n
    return int(n*(n+1)/2)

def sum_squares(n_list: list) -> float:
    return sum([x**2 for x in n_list])

def iterable_product(iter) -> float:
    ip = 1
    for n in iter:
        ip *= n
    return ip

def lcm_pf(*args: int) -> Counter:
    # returns the lcm as a prime factorization from a set of ints
    counters = map(primes.prime_factorization,args)
    lcm_pf_counter = Counter()
    for c in counters:
        lcm_pf_counter |= c
    return lcm_pf_counter

def lcm(*args: int) -> int:
    # returns the lcm as an int from a set of ints
    return primes.num_from_pf_counter(lcm_pf(*args))

def gcf_pf(*args: int) -> Counter:
    # returns the gcf as a prime factorization from a set of ints
    counters = map(primes.prime_factorization,args)
    gcf_pf_counter = Counter()
    for c in counters:
        gcf_pf_counter |= c
    for c in counters:
        gcf_pf_counter &= c
    return gcf_pf_counter

def gcf(*args: int) -> int:
    # returns the gcf as an int from a set of ints
    return primes.num_from_pf_counter(gcf_pf(*args))

def divisor_count_from_pf(pf: Counter) -> int:
    # returns a count of all the divisors from a prime factorization
    prod = iterable_product(map(lambda x: x+1,pf.values()))
    return prod

def divisor_count(n: int) -> int:
    # returns a count of all the divisors of an integer
    pf = primes.prime_factorization(n)
    return divisor_count_from_pf(pf)

def divisors(n: int) -> list:
    # returns all the divisors of an integer
    if n == 1:
        return [1]
    pf = primes.prime_factorization(n)
    divs = [1]
    tracker = dict(pf)
    while max(tracker.values())>0:
        divs.append(primes.num_from_pf_counter(tracker))
        for factor in tracker:
            if tracker[factor] > 0:
                tracker[factor] -= 1
                break
            else:
                tracker[factor] = pf[factor]
    divs.sort()
    return divs

def factorial(n: int) -> int:
    # == n!
    return iterable_product(range(1,n+1))

def partial_factorial(n: int, k: int) -> int:
    # == n!/k!
    return iterable_product(range(k+1,n+1))

def n_choose_k(n: int,k: int) -> int:
    # == nCk
    return partial_factorial(n,k) // factorial(n-k)





