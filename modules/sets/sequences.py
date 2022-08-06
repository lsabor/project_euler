"""sequences"""
from math import sqrt
from sets.sets import *


class Sequence(Set):
    """a generic sequence"""

    name = "Sequence"
    example = "[s1 s2 s3 ...]"
    indexed = True
    first_index = 0
    first_value = ...

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cardinality = Cardinality("N0")

    def formula(self, n):
        ...


class FormulaicSequence(Sequence):
    """a sequence where nth element can be computed directly from n"""

    name = "Formulaic Sequence"
    example = "[f(0) f(1) f(2) ...]"


class InvertableFormulaicSequence(FormulaicSequence):
    """a sequence where nth element can be computed directly from n and vice versa"""

    name = "Invertable Formulaic Sequence"
    example = "[f(0) f(1) f(2) ...] where f: N <-> X"

    def inverseFormula(self, n):
        ...

    def getIndex(self, n):
        """gets the index of n"""
        self.test(n)
        return self.inverseFormula(n)

    def getNext(self, n):
        """gets the succeeding value of n"""
        self.test(n)
        index = self.getIndex(n)
        return self.formula(n + 1)

    def getPrevious(self, n):
        """gets the succeeding value of n"""
        self.test(n)
        index = self.getIndex(n)
        if index == self.first_index:
            raise ValueError(f"There is no predecessor to {n=} in {self.name}")
        return self.formula(n - 1)

    @classmethod
    def _isInSet(self, n) -> bool:
        return (self.inverseFormula(n) % 1) == 0

    @classmethod
    def isInSet(self, n):
        return self._isInSet(n) and super().isInSet(n)


class IterativeSequence(Sequence):
    """a sequence where nth element is computer from previous element(s)"""

    name = "Iterative Sequence"
    example = "[f(0) f(f(0)) f(f(f(0))) ...]"

    def getNext(self, n):
        ...

    def formula(self, n):
        if n == self.first_index:
            return self.first_value
        return self.getNext(self.formula(n - 1))


class InverseIterativeSequence(IterativeSequence):
    """a sequence where nth element is computer from previous element(s) and vice versa"""

    name = "Inverse Iterative Sequence"
    example = "[f-1(f-1(0)) f-1(0) 0 f(0) ...]"

    def getPrevious(self, n):
        ...

    def inverseFormula(self, n):
        index = self.first_index
        while n != self.first_value:
            index += 1
            n = self.getPrevious(n)
        return index


class TriangleNumbers(InvertableFormulaicSequence, Naturals):
    """triangle numbers"""

    name = "Triangle Numbers"
    example = "[1 3 6 10 ...]"

    @staticmethod
    def formula(n: int):
        """returns the nth Triangle Number"""
        return int(n * (n + 1) / 2)

    @staticmethod
    def inverseFormula(n):
        return sqrt(2 * n + 1 / 4) - 1 / 2


class SquareNumbers(InvertableFormulaicSequence, Naturals):
    """Square numbers"""

    name = "Square Numbers"
    example = "[1 4 9 16 ...]"

    @staticmethod
    def formula(n: int):
        """returns the nth Square Number"""
        return int(n * n)

    @staticmethod
    def inverseFormula(n):
        return sqrt(n)


class PentagonalNumbers(InvertableFormulaicSequence, Naturals):
    """Pentagonal numbers"""

    name = "Pentagonal Numbers"
    example = "[1 5 12 22 ...]"

    @staticmethod
    def formula(n: int):
        """returns the nth Pentagonal Number"""
        return int(n * (3 * n - 1) / 2)

    @staticmethod
    def inverseFormula(n):
        return (2 * sqrt(6 * n + 1 / 4) + 1) / 6


class HexagonalNumbers(InvertableFormulaicSequence, Naturals):
    """Hexagonal numbers"""

    name = "Hexagonal Numbers"
    example = "[1 6 15 28 ...]"

    @staticmethod
    def formula(n: int):
        """returns the nth Hexagonal Number"""
        return int(n * (2 * n - 1))

    @staticmethod
    def inverseFormula(n):
        return sqrt(2 * n + 1 / 4) / 2 + 1 / 4


class HeptagonalNumbers(InvertableFormulaicSequence, Naturals):
    """Heptagonal numbers"""

    name = "Heptagonal Numbers"
    example = "[1 7 18 34 ...]"

    @staticmethod
    def formula(n: int):
        """returns the nth Heptagonal Number"""
        return int(n * (5 * n - 3) / 2)

    @staticmethod
    def inverseFormula(n):
        return (2 * sqrt(10 * n + 9 / 4) + 3) / 10


class OctagonalNumbers(InvertableFormulaicSequence, Naturals):
    """Octagonal numbers"""

    name = "Octagonal Numbers"
    example = "[1 8 21 40 ...]"

    @staticmethod
    def formula(n: int):
        """returns the nth Octagonal Number"""
        return int(n * (3 * n - 2))

    @staticmethod
    def inverseFormula(n):
        return (sqrt(3 * n + 1) + 1) / 3
