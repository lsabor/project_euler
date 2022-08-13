"""specific sets like the Reals"""


from collections import Counter
from sets.sets import *


def isPrime(n: int) -> bool:
    """uses Miller-Rabin primality test
    only effective up to 3,317,044,064,679,887,385,961,981"""
    if (n < 2) or (n % 2 == 0):
        return False
    if n == 2:
        return True
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
        raise ValueError(f"{n=} too big to handle with this test")

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


class Ints(Set):
    """Set of integers"""

    name = "Integers"
    example = "{... -2 -1 0 1 2 ...}"
    ordered = True
    cardinality = Cardinality("N0")

    @classmethod
    def _isInSet(self, n: Number) -> bool:
        """return if n passes the test unique to Ints
        but not classes it inherits from"""
        try:
            return float(n).is_integer()
        except:
            return False


class Naturals(Ints):
    """Set of natural numbers"""

    name = "Naturals Numbers"
    example = "{0 1 2 3 ...}"

    @classmethod
    def _isInSet(self, n: Number) -> bool:
        """return if n passes the test unique to Natural numbers
        but not classes it inherits from"""
        return n >= 0


class Primes(Naturals):
    """Set of prime numbers"""

    name = "Primes"
    example = "{2 3 5 7 11 ...}"

    @staticmethod
    def isPrime(n: int) -> bool:
        return isPrime(n)

    @classmethod
    def _isInSet(self, n: Number) -> bool:
        return self.isPrime(n)


class PrimeFactorizations(Set):
    """Set of prime factorizations"""

    name = "PrimeFactorizations"
    example = "{Counter({}) Counter({}) Counter({2:1}) Counter({3:1}) ...}"
