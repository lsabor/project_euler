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
from itertools import chain, combinations


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


def is_divisible(n: Number, d: Number) -> bool:
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
        result = raise_power_modulo(result, n, mod=mod)
    return result


def powerset(iterable):
    """returns all subsets of a set"""
    xs = list(iterable)
    return chain.from_iterable(combinations(xs, n) for n in range(len(xs) + 1))


class SpecialNumbers:
    """DOCSTRING"""

    name = "SpecialNumbers"
    example = "[literally anything?]"
    formula = None
    ordered = False
    indexed = False
    cardinality = None
    cyclic = False

    def __init__(self, *args, **kwargs):
        pass

    def __repr__(self):
        return self.example

    def __getitem__(self, index):
        if not self.indexed:
            raise TypeError(f"{self.name} is not indexed")
        if not self.cyclic:
            if (index < 1) or (index % 1 != 0):
                raise ValueError(f"{index = } must be a natrual number")
        return self.nth(index)

    def __gt__(self, other):
        if not self.ordered:
            raise TypeError(f"{self.name} is not ordered")
        return self.value > other.value

    def __lt__(self, other):
        if not self.ordered:
            raise TypeError(f"{self.name} is not ordered")
        return self.value < other.value

    def __ge__(self, other):
        if not self.ordered:
            raise TypeError(f"{self.name} is not ordered")
        return self.value >= other.value

    def __le__(self, other):
        if not self.ordered:
            raise TypeError(f"{self.name} is not ordered")
        return self.value <= other.value

    def __eq__(self, other):
        if not self.ordered:
            raise TypeError(f"{self.name} is not ordered")
        return self.value == other.value

    def size(self):
        return self.cardinality

    def getNext(self, n):
        if not self.indexed:
            raise TypeError(f"{self.name} is not indexed")
        return self.nth(self.getIndex(n) + 1)

    def errString(self, value):
        return f"{value} is not a {self.name}. E.g. {self.example}"


class Cardinalities(SpecialNumbers):
    """docstring"""

    name = "Cardinalities"
    example = "[0 1 2 ... N0 N1 N2 ...]"
    ordered = True

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

    @staticmethod
    def isCardinality(card: int or str) -> bool:
        """return is card is a cardinality"""
        if type(card) == str:
            if len(card) < 2:
                return False
            if card[0] != "N":
                return False
            try:
                int(card[1:])
                return True
            except:
                return False
        else:
            return float(card).is_integer()

    def __gt__(self, other):
        if self.order != other.order:
            return self.order > other.order
        return self.value > other.value

    def __lt__(self, other):
        if self.order != other.order:
            return self.order < other.order
        return self.value < other.value

    def __ge__(self, other):
        if self.order != other.order:
            return self.order > other.order
        return self.value >= other.value

    def __le__(self, other):
        if self.order != other.order:
            return self.order < other.order
        return self.value <= other.value

    def __eq__(self, other):
        return (self.order == other.order) and (self.value == other.value)


class Cardinality(Cardinalities):
    """cardinality property"""

    name = "Cardinality"

    def __init__(self, cardinality, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        assert Cardinalities.isCardinality(cardinality), self.errString(cardinality)
        if type(cardinality) == str:
            self.order = 1
            self.value = int(cardinality[1:])
        else:
            self.order = 0
            self.value = cardinality

    def __repr__(self):
        string = "N" if self.order else ""
        string += str(self.value)
        return string


class Ints(SpecialNumbers):
    """integer type numbers"""

    name = "Integers"
    example = "[...-3 -2 -1 0 1 2 3...]"
    ordered = True
    cardinality = Cardinality("N0")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def isInt(n: Number) -> bool:
        """returns if n is an Int"""
        try:
            return float(n).is_integer()
        except:
            return False


class Int(Ints):
    """a specific Integer"""

    name = "Int"
    cardinality = Cardinality(1)

    def __init__(self, n: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        assert Ints.isInt(n), self.errString(n)
        self.value = int(n)

    def __repr__(self):
        return str(self.value)


class Naturals(Ints):
    """natural number types"""

    name = "Naturals"
    example = "[0 1 2 3 ...]"
    formula = "n"
    indexed = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def isNatural(n: Number) -> bool:
        """returns if n is a Natural number"""
        return n >= 0

    @staticmethod
    def nth(n):
        if (n < 0) or (n % 1 != 0):
            raise ValueError(f"{n=} must be a natrual number")
        return Natural(n)

    def getIndex(self, n) -> int:
        """gets the index of n"""
        if type(n) == Natural:
            n = n.value
        if n % 1 == 0:
            return int(n)
        raise ValueError(self.errString(n))

    @staticmethod
    def inverseFormula(n):
        return n


class Natural(Int, Naturals):
    """a particular natural number"""

    name = "Natural"

    def __init__(self, n: int, *args, **kwargs):
        super().__init__(n=n, *args, **kwargs)
        assert Naturals.isNatural(n), self.errString(n)
        self.value = int(n)


class TriangleNumbers(Naturals):
    """triangle numbers"""

    name = "Triangle Numbers"
    example = "[1 3 6 10 ...]"
    formula = "n*(n+1)/2"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def isTriangleNumber(n: Number) -> bool:
        """returns if n is a Triangle Number"""
        return TriangleNumbers.inverseFormula(n) % 1 == 0

    @staticmethod
    def nth(n: int):
        """returns the nth Triangle Number"""
        return TriangleNumber(int(n * (n + 1) / 2))

    def getIndex(self, n) -> int:
        """gets the index of n"""
        if type(n) == TriangleNumber:
            n = n.value
        index = TriangleNumbers.inverseFormula(n)
        if index % 1 == 0:
            return int(index)
        raise ValueError(self.errString(n))

    @staticmethod
    def inverseFormula(n):
        return sqrt(2 * n + 1 / 4) - 1 / 2


class TriangleNumber(TriangleNumbers, Natural):
    """a particular triangle number"""

    name = "Triangle Number"

    def __init__(self, n: int, *args, **kwargs):
        super().__init__(n=n, *args, **kwargs)
        assert TriangleNumbers.isTriangleNumber(n), self.errString(n)
        self.value = int(n)


class SquareNumbers(Naturals):
    """Square numbers"""

    name = "Square Numbers"
    example = "[1 4 9 16 ...]"
    formula = "n*n"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def isSquareNumber(n: Number) -> bool:
        """returns if n is a Square Number"""
        return SquareNumbers.inverseFormula(n) % 1 == 0

    @staticmethod
    def nth(n: int):
        """returns the nth Square Number"""
        return SquareNumber(int(n * n))

    def getIndex(self, n) -> int:
        """gets the index of n"""
        if type(n) == SquareNumber:
            n = n.value
        index = SquareNumbers.inverseFormula(n)
        if index % 1 == 0:
            return int(index)
        raise ValueError(self.errString(n))

    @staticmethod
    def inverseFormula(n):
        return sqrt(n)


class SquareNumber(SquareNumbers, Natural):
    """a particular Square number"""

    name = "Square Number"

    def __init__(self, n: int, *args, **kwargs):
        super().__init__(n=n, *args, **kwargs)
        assert SquareNumbers.isSquareNumber(n), self.errString(n)
        self.value = int(n)


class PentagonalNumbers(Naturals):
    """Pentagonal numbers"""

    name = "Pentagonal Numbers"
    example = "[1 5 12 22 ...]"
    formula = "n*(3*n-1)/2"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def isPentagonalNumber(n: Number) -> bool:
        """returns if n is a Pentagonal Number"""
        return PentagonalNumbers.inverseFormula(n) % 1 == 0

    @staticmethod
    def nth(n: int):
        """returns the nth Pentagonal Number"""
        return PentagonalNumber(int(n * (3 * n - 1) / 2))

    def getIndex(self, n) -> int:
        """gets the index of n"""
        if type(n) == PentagonalNumber:
            n = n.value
        index = PentagonalNumbers.inverseFormula(n)
        if index % 1 == 0:
            return int(index)
        raise ValueError(self.errString(n))

    @staticmethod
    def inverseFormula(n):
        return (2 * sqrt(6 * n + 1 / 4) + 1) / 6


class PentagonalNumber(PentagonalNumbers, Natural):
    """a particular Pentagonal number"""

    name = "Pentagonal Number"

    def __init__(self, n: int, *args, **kwargs):
        super().__init__(n=n, *args, **kwargs)
        assert PentagonalNumbers.isPentagonalNumber(n), self.errString(n)
        self.value = int(n)


class HexagonalNumbers(Naturals):
    """Hexagonal numbers"""

    name = "Hexagonal Numbers"
    example = "[1 6 15 28 ...]"
    formula = "n*(2*n-1)"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def isHexagonalNumber(n: Number) -> bool:
        """returns if n is a Hexagonal Number"""
        return HexagonalNumbers.inverseFormula(n) % 1 == 0

    @staticmethod
    def nth(n: int):
        """returns the nth Hexagonal Number"""
        return HexagonalNumber(int(n * (2 * n - 1)))

    def getIndex(self, n) -> int:
        """gets the index of n"""
        if type(n) == HexagonalNumber:
            n = n.value
        index = HexagonalNumbers.inverseFormula(n)
        if index % 1 == 0:
            return int(index)
        raise ValueError(self.errString(n))

    @staticmethod
    def inverseFormula(n):
        return sqrt(2 * n + 1 / 4) / 2 + 1 / 4


class HexagonalNumber(HexagonalNumbers, Natural):
    """a particular Hexagonal number"""

    name = "Hexagonal Number"

    def __init__(self, n: int, *args, **kwargs):
        super().__init__(n=n, *args, **kwargs)
        assert HexagonalNumbers.isHexagonalNumber(n), self.errString(n)
        self.value = int(n)


class HeptagonalNumbers(Naturals):
    """Heptagonal numbers"""

    name = "Heptagonal Numbers"
    example = "[1 7 18 34 ...]"
    formula = "n*(5*n-3)/2"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def isHeptagonalNumber(n: Number) -> bool:
        """returns if n is a Heptagonal Number"""
        return HeptagonalNumbers.inverseFormula(n) % 1 == 0

    @staticmethod
    def nth(n: int):
        """returns the nth Heptagonal Number"""
        return HeptagonalNumber(int(n * (5 * n - 3) / 2))

    def getIndex(self, n) -> int:
        """gets the index of n"""
        if type(n) == HeptagonalNumber:
            n = n.value
        index = HeptagonalNumbers.inverseFormula(n)
        if index % 1 == 0:
            return int(index)
        raise ValueError(self.errString(n))

    @staticmethod
    def inverseFormula(n):
        return (2 * sqrt(10 * n + 9 / 4) + 3) / 10


class HeptagonalNumber(HeptagonalNumbers, Natural):
    """a particular Heptagonal number"""

    name = "Heptagonal Number"

    def __init__(self, n: int, *args, **kwargs):
        super().__init__(n=n, *args, **kwargs)
        assert HeptagonalNumbers.isHeptagonalNumber(n), self.errString(n)
        self.value = int(n)


class OctagonalNumbers(Naturals):
    """Octagonal numbers"""

    name = "Octagonal Numbers"
    example = "[1 8 21 40 ...]"
    formula = "n*(3*n-2)"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def isOctagonalNumber(n: Number) -> bool:
        """returns if n is a Octagonal Number"""
        return OctagonalNumbers.inverseFormula(n) % 1 == 0

    @staticmethod
    def nth(n: int):
        """returns the nth Octagonal Number"""
        return OctagonalNumber(int(n * (3 * n - 2)))

    def getIndex(self, n) -> int:
        """gets the index of n"""
        if type(n) == OctagonalNumber:
            n = n.value
        index = OctagonalNumbers.inverseFormula(n)
        if index % 1 == 0:
            return int(index)
        raise ValueError(self.errString(n))

    @staticmethod
    def inverseFormula(n):
        return (sqrt(3 * n + 1) + 1) / 3


class OctagonalNumber(OctagonalNumbers, Natural):
    """a particular Octagonal number"""

    name = "Octagonal Number"

    def __init__(self, n: int, *args, **kwargs):
        super().__init__(n=n, *args, **kwargs)
        assert OctagonalNumbers.isOctagonalNumber(n), self.errString(n)
        self.value = int(n)
