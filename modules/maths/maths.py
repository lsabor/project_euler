# This module holds basic math functions

from numbers import Number
from typing import Generator, Iterable, Mapping
import primes

# from sequences import Prime_Factorizations # TODO fixxxxx
from collections import Counter
from math import sqrt
from functools import reduce
from operator import add
from itertools import permutations as perms, product
from itertools import chain, combinations


def sumConsecutiveInts(n: int) -> int:
    # returns sum of consecutive ints up to and including n
    return int(n * (n + 1) / 2)


def sumSquares(n_list: list) -> float:
    # returns sum on squares of a list
    return sum([x**2 for x in n_list])


def iterableProduct(iter) -> float:
    """returns the cumulative product of the iterable object given"""
    ip = 1
    for n in iter:
        ip *= n
    return ip


def smartPFCounter(n, PF=None) -> Counter:
    # PF = PF if PF else Prime_Factorizations()
    # if len(PF) >= n:
    # return PF[n]
    return primes.prime_factorization(n)


def lcmPF(*args: int, PF=None) -> Counter:
    # returns the lcm as a prime factorization from a set of ints
    counters = [smartPFCounter(n, PF=PF) for n in args]
    lcmPFCounter = Counter()
    for c in counters:
        lcmPFCounter |= c
    return lcmPFCounter


def lcm(*args: int, PF=None) -> int:
    # returns the lcm as an int from a set of ints
    return primes.numFromPFCounter(lcmPF(*args, PF=PF))


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
    return primes.numFromPFCounter(gcfPF(*args, PF=PF))


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
    return divs


def divisors(n: int) -> list:
    # returns all the divisors of an integer
    if n == 1:
        return [1]
    pf = smartPFCounter(n)
    return divisorsFromPFCounter(pf)


def properDivisors(n: int) -> list:
    # returns divisors of n not including n
    return divisors(n)[:-1]


def factorial(n: int) -> int:
    # == n!
    return iterableProduct(range(1, n + 1))


def partialFactorial(n: int, k: int) -> int:
    # == n!/k!
    return iterableProduct(range(k + 1, n + 1))


def nChoosek(n: int, k: int) -> int:
    # == nCk
    return partialFactorial(n, k) // factorial(n - k)


def sumOfDigits(n: int) -> int:
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


def stringPermutations(string: str) -> Mapping:
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


def squareRoot(n, precision=5):
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


def isDivisible(n: Number, d: Number) -> bool:
    """tests if n is divisible by d"""
    return n % d == 0


def modex(b, e, m):
    """returns n to the xth power modulo mod at each step"""
    if m == 1:
        return 0
    result = 1
    b %= m
    while e:
        if (e % 2) == 1:
            result = (result * b) % m
        e >>= 1
        b = (b * b) % m
    return result


def tetrate(n, depth=2, mod=0):
    """gives the tetration depth levels deep of n"""
    if (not depth) or (depth % 1 != 0):
        raise ValueError("depth must be an integer greater than 0")

    result = n
    for _ in range(depth - 1):
        result = modex(result, n, mod=mod)
    return result


def powerset(iterable):
    """returns all subsets of a set"""
    xs = list(iterable)
    return chain.from_iterable(combinations(xs, n) for n in range(len(xs) + 1))


def areRelativePrimes(n: int, m: int) -> bool:
    """n and m are relatively prime if their gcf is 1"""
    return gcf(n, m) == 1


def totient(n: int) -> int:
    """counts all ints < n which are relatively prime to n"""
    count = 0
    for m in range(1, n):
        count += areRelativePrimes(n, m)
    return count
