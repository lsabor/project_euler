""" stores specific sequences 
any sequence that inherits from another sequences
is a subsequence"""

from maths.sequences.sequences import *
from maths.sets import *
from math import log as ln
from math import ceil, sqrt
from decimal import Decimal


class IntsSeq(Ints, InvertableSequence):
    """Integers as a sequence"""

    name = "IntegersSequence"
    example = "[0, 1, -1, 2, -2, ...]"
    indexed = True
    first_value = 0

    @staticmethod
    def formula(n: int) -> int:
        """returns the nth int from [0, 1, -1, 2, -2, ...]"""
        return int((n + 1) // 2 * (2 * (n % 2) - 1))

    @staticmethod
    def inverseFormula(n: int) -> int:
        """returns the index for the interger n from [0, 1, -1, 2, -2, ...]"""
        return abs(2 * n) + (n <= 0) - 1


class NatsSeq(Naturals, InvertableSequence):
    """Natural Numbers as a sequence"""

    name = "NaturalsSequence"
    example = "[0 1 2 3 ...]"
    first_value = 0
    monotonic = 1

    @staticmethod
    def formula(n: int) -> int:
        return n

    @staticmethod
    def inverseFormula(n: Number) -> int:
        return n

    def approxCount(self, n: int) -> int:
        """returns the expected index of a given n"""
        return int(self.inverseFormula(n))


class PrimesSeq(Primes, TestOnlySequence):
    """Prime numbers in order"""

    name = "PrimesSequence"
    example = "[2 3 5 7 11 ...]"
    first_value = 2
    monotonic = 1
    cached = True

    def nextToTest(self, n: int) -> int:
        return n + 1

    def isInSet(self, n: int) -> bool:
        return self._isInSet(n)

    def approxCount(self, n: int) -> int:
        """returns an approximation of how many primes exist below n"""
        return int(n / ln(n))


class TriangleNumbers(NatsSeq):
    """triangle numbers"""

    name = "TriangleNumbers"
    example = "[1 3 6 10 ...]"
    first_value = 1

    @staticmethod
    def formula(n: int) -> int:
        """returns the nth Triangle Number"""
        n = n + 1
        return int(n * (n + 1) / 2)

    @staticmethod
    def inverseFormula(n: Number) -> Number:
        n = Decimal(str(n))
        return float((Decimal("2") * n + Decimal(1 / 4)).sqrt() - Decimal(1 / 2)) - 1


class SquareNumbers(NatsSeq):
    """Square numbers"""

    name = "SquareNumbers"
    example = "[1 4 9 16 ...]"
    first_value = 1

    @staticmethod
    def formula(n: int) -> int:
        """returns the nth Square Number"""
        n += 1
        return int(n * n)

    @staticmethod
    def inverseFormula(n: Number) -> int:
        n = Decimal(str(n))
        return float(n.sqrt()) - 1


class PentagonalNumbers(NatsSeq):
    """Pentagonal numbers"""

    name = "PentagonalNumbers"
    example = "[1 5 12 22 ...]"
    first_value = 1

    @staticmethod
    def formula(n: int) -> int:
        """returns the nth Pentagonal Number"""
        n += 1
        return int(n * (3 * n - 1) / 2)

    @staticmethod
    def inverseFormula(n: Number) -> int:
        return ((2 * sqrt(6 * n + 1 / 4) + 1) / 6) - 1


class HexagonalNumbers(NatsSeq):
    """Hexagonal numbers"""

    name = "HexagonalNumbers"
    example = "[1 6 15 28 ...]"
    first_value = 1

    @staticmethod
    def formula(n: int) -> int:
        """returns the nth Hexagonal Number"""
        n += 1
        return int(n * (2 * n - 1))

    @staticmethod
    def inverseFormula(n: Number) -> int:
        return (sqrt(2 * n + 1 / 4) / 2 + 1 / 4) - 1


class HeptagonalNumbers(NatsSeq):
    """Heptagonal numbers"""

    name = "HeptagonalNumbers"
    example = "[1 7 18 34 ...]"
    first_value = 1

    @staticmethod
    def formula(n: int) -> int:
        """returns the nth Heptagonal Number"""
        n += 1
        return int(n * (5 * n - 3) / 2)

    @staticmethod
    def inverseFormula(n: Number) -> int:
        return ((2 * sqrt(10 * n + 9 / 4) + 3) / 10) - 1


class OctagonalNumbers(NatsSeq):
    """Octagonal numbers"""

    name = "OctagonalNumbers"
    example = "[1 8 21 40 ...]"
    first_value = 1

    @staticmethod
    def formula(n: int) -> int:
        """returns the nth Octagonal Number"""
        n += 1
        return int(n * (3 * n - 2))

    @staticmethod
    def inverseFormula(n: Number) -> int:
        return ((sqrt(3 * n + 1) + 1) / 3) - 1


class Fibonacci(NatsSeq):
    """Fibonacci numbers"""

    name = "FibonacciNumbers"
    example = "[1 1 2 3 5 8 13 ...]"
    first_value = 1

    @staticmethod
    def formula(n: int) -> int:
        """returns the nth fibonacci number"""
        if n < 2:
            return 1
        Phi = (1 + sqrt(5)) / 2
        phi = (1 - sqrt(5)) / 2
        f = (Phi ** (n + 1) + phi ** (n + 1)) / sqrt(5)
        return round(f)

    @staticmethod
    def inverseFormula(f: int) -> int:
        """returns n from a given fibonnaci number f"""
        Phi = (1 + sqrt(5)) / 2
        n = ceil(ln(f * sqrt(5) - 0.5, Phi))
        return n - 1

    def _isInSetSpecified(self, n: int) -> bool:
        return n == self.formula(self.inverseFormula(n))
