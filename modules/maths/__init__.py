# This module holds basic math functions

from numbers import Number
from typing import Generator, Iterable, Mapping
import primes
from sequences import Prime_Factorizations
from collections import Counter
from math import sqrt
from functools import reduce
from operator import add
from itertools import permutations as perms


def sum_consecutive_ints(n: int) -> int:
    # returns sum of consecutive ints up to and including n
    return int(n * (n + 1) / 2)


def sum_squares(n_list: list) -> float:
    # returns sum on squares of a list
    return sum([x**2 for x in n_list])


def iterable_product(iter) -> float:
    """returns the cumulative product of the iterable object given"""
    ip = 1
    for n in iter:
        ip *= n
    return ip


def smart_pf_counter(n, PF=None) -> Counter:
    PF = PF if PF else Prime_Factorizations()
    if len(PF) >= n:
        return PF[n]
    return primes.prime_factorization(n)


def lcm_pf(*args: int, PF=None) -> Counter:
    # returns the lcm as a prime factorization from a set of ints
    counters = [smart_pf_counter(n, PF=PF) for n in args]
    lcm_pf_counter = Counter()
    for c in counters:
        lcm_pf_counter |= c
    return lcm_pf_counter


def lcm(*args: int, PF=None) -> int:
    # returns the lcm as an int from a set of ints
    return primes.num_from_pf_counter(lcm_pf(*args, PF=PF))


def gcf_pf(*args: int, PF=None) -> Counter:
    # returns the gcf as a prime factorization from a set of ints
    counters = [smart_pf_counter(n, PF=PF) for n in args]
    gcf_pf_counter = Counter()
    for c in counters:
        gcf_pf_counter |= c
    for c in counters:
        gcf_pf_counter &= c
    return gcf_pf_counter


def gcf(*args: int, PF=None) -> int:
    # returns the gcf as an int from a set of ints
    return primes.num_from_pf_counter(gcf_pf(*args, PF=PF))


def divisor_count_from_pf_counter(pf: Counter) -> int:
    # returns a count of all the divisors from a prime factorization
    prod = iterable_product(map(lambda x: x + 1, pf.values()))
    return prod


def divisor_count(n: int) -> int:
    # returns a count of all the divisors of an integer
    pf = smart_pf_counter(n)
    return divisor_count_from_pf_counter(pf)


def divisors_from_pf_counter(pf: Counter) -> list:
    divs = [1]
    tracker = dict(pf)
    while max(tracker.values()) > 0:
        divs.append(primes.num_from_pf_counter(tracker))
        for factor in tracker:
            if tracker[factor] > 0:
                tracker[factor] -= 1
                break
            else:
                tracker[factor] = pf[factor]
    divs.sort()
    return divs


def divisors(n: int) -> list:
    # returns all the divisors of an integer
    if n == 1:
        return [1]
    pf = smart_pf_counter(n)
    return divisors_from_pf_counter(pf)


def proper_divisors(n: int) -> list:
    # returns divisors of n not including n
    return divisors(n)[:-1]


def factorial(n: int) -> int:
    # == n!
    return iterable_product(range(1, n + 1))


def partial_factorial(n: int, k: int) -> int:
    # == n!/k!
    return iterable_product(range(k + 1, n + 1))


def n_choose_k(n: int, k: int) -> int:
    # == nCk
    return partial_factorial(n, k) // factorial(n - k)


def sum_of_digits(n: int) -> int:
    # in base 10
    return sum([int(digit) for digit in str(n)])


def permutations(ls):
    """returns a list of all permutations of the list
    Just use itertools.permutations though, this is just a proof of concept"""
    if len(ls) > 2:
        perms = []
        first = ls[0]
        rest = ls[1:]
        for perm in permutations(rest):
            for j in range(len(perm) + 1):
                perms.append(perm[:j] + [first] + perm[j:])
        return perms
    elif len(ls) == 2:
        return [ls, [ls[1], ls[0]]]
    return [ls]


def string_permutations(string: str) -> Mapping:
    """returns all permutations of a string"""
    return map(lambda x: reduce(add, x), perms(string))


def combinations(ls, n):
    """just use itertools combinations though"""
    # returns a list of all combinations (in order of ls) of n elements from list
    length = len(ls)
    if n == 0 or length < n:
        return [[]]
    if length == n:
        return [ls]
    if length > n:
        first = ls[0]
        rest = ls[1:]
        combs = []
        for comb in combinations(rest, n - 1):
            combs.append([first] + comb)
        for comb in combinations(rest, n):
            combs.append(comb)
        return combs


def square_root(n, precision=5):
    """finds the square root of n up to precision decimal places.
    This is just a proof of concept, just use math.sqrt"""
    if n < 0:
        raise ValueError("cannot square root numbers less than 0 with this function")
    if n == 0:
        return 0
    if n == 1:
        return 1

    larger = n > 1

    r = 1  # root, the number we're looking for
    upper = 1  # the upper bound for r
    lower = 1  # the lower bound for r
    m = 0

    if larger:
        while r**2 < n:
            lower = r
            r *= 2
            m = r
        upper = r
    else:
        while r**2 > n:
            upper = r
            r *= 0.5
            m = -r
        lower = r

    # keep iterating until the movement rounded to precision decimal places is 0
    while round(m, precision) != 0:
        estimate = r**2
        if n == estimate:
            return round(r, precision)  # we are done
        elif n > estimate:
            lower = r
        else:
            upper = r
        r = lower + (upper - lower) / 2
        m = r - lower

    return round(r, precision)


def ceil(n):
    """gets the ceiling of n"""
    if n % 1 == 0:
        return n
    return int(n) + 1


def floor(n):
    """gets the floor of n"""
    return int(n)


def is_triangle_number(n: Number) -> bool:
    """tests if n is a triangle number"""
    # t_i is the ith triangle number
    # t_i = (1/2)*i*(i+1)
    # i = sqrt(2*t_i + 1/4) - 1/2
    # thus let t_i = n, and see if i is a whole number
    if (n < 1) or (n % 1 != 0):
        return False
    return (sqrt(2 * n + 1 / 4) - 1 / 2) % 1 == 0


def is_pentagonal_number(n: Number) -> bool:
    """tests if n is a pentagonal number"""
    if (n < 1) or (n % 1 != 0):
        return False
    return ((2 * sqrt(6 * n + 1 / 4) + 1) / 6) % 1 == 0


def is_hexagonal_number(n: Number) -> bool:
    """tests if n is a hexagonal number"""
    if (n < 1) or (n % 1 != 0):
        return False
    return (sqrt(2 * n + 1 / 4) / 2 + 1 / 4) % 1 == 0


def is_divisible(n: Number, d: Number) -> bool:
    """tests if n is divisible by d"""
    return n % d == 0
