# This module holds info about Sets

from numbers import Number
from math import sqrt


class Set:
    """A collection of things"""

    name = "Set"
    example = "A collection of literally anything"
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
        return self.comparitor > other.comparitor

    def __eq__(self, other):
        if not self.ordered:
            raise TypeError(f"{self.name} is not ordered")
        return self.comparitor == other.comparitor

    @classmethod
    def size(self):
        return self.cardinality

    def getNext(self, n):
        if not self.indexed:
            raise TypeError(f"{self.name} is not indexed")
        return self.nth(self.getIndex(n) + 1)

    def errString(self, value):
        return f"{value} is not a {self.name}. E.g. {self.example}"


class Cardinalities(Set):
    """Cardinality given to a set. Cardinalities is a set itself of course.
    includes the natural numbers and Alephs (N0 N1 ...)
    generally indicates the size of a set"""

    name = "Cardinalities"
    example = "[0 1 2 ... N0 N1 N2 ...]"
    ordered = True

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

    @staticmethod
    def isCardinality(card: int or str) -> bool:
        """return if input is a cardinality"""
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
        if not isinstance(other, type(self)):
            raise TypeError(f"{type(other)} cannot be compared to {type(self)}")
        if self.order != other.order:
            return self.order > other.order
        return self.value > other.value

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(f"{type(other)} cannot be compared to {type(self)}")
        return (self.order == other.order) and (self.value == other.value)


class Cardinality(Cardinalities):
    """A specific Cardinality"""

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


class Ints(Set):
    """Integers"""

    name = "Integers"
    example = "[...-3 -2 -1 0 1 2 3...]"
    ordered = True
    cardinality = Cardinality("N0")
    comparitor = cardinality

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def _isNatural(n: Number) -> bool:
        """return if n passes the test unique to Natural numbers
        but not classes it inherits from"""
        return n >= 0

    @staticmethod
    def isNatural(n: Number) -> bool:
        """returns if n is a Natural number"""
        return Naturals._isNatural(n) and Ints.isInt(n)

    @staticmethod
    def _isInt(n: Number) -> bool:
        """return if n passes the test unique to Ints
        but not classes it inherits from"""
        try:
            return float(n).is_integer()
        except:
            return False

    @staticmethod
    def isInt(n: Number) -> bool:
        print("RUNNING ISINT")
        """returns if n is an Int"""
        return Ints._isInt(n)


class Int(Ints):
    """a specific Integer"""

    name = "Int"
    cardinality = Cardinality(1)

    def __init__(self, n: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        assert Ints._isInt(n), self.errString(n)
        self.value = int(n)
        self.comparitor = self.value

    def __repr__(self):
        return str(self.value)


class Naturals(Ints):
    """Natural Numbers"""

    name = "Naturals"
    example = "[0 1 2 3 ...]"
    formula = "n"
    indexed = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def _isNatural(n: Number) -> bool:
        """return if n passes the test unique to Natural numbers
        but not classes it inherits from"""
        return n >= 0

    @staticmethod
    def isNatural(n: Number) -> bool:
        """returns if n is a Natural number"""
        return Naturals._isNatural(n) and Ints.isInt(n)

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
        assert Naturals._isNatural(n), self.errString(n)
        self.value = int(n)


class TriangleNumbers(Naturals):
    """triangle numbers"""

    name = "Triangle Numbers"
    example = "[1 3 6 10 ...]"
    formula = "n*(n+1)/2"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def _isTriangleNumber(n: Number) -> bool:
        """return if n passes the test unique to Triangle numbers
        but not classes it inherits from"""
        return TriangleNumbers.inverseFormula(n) % 1 == 0

    @staticmethod
    def isTriangleNumber(n: Number) -> bool:
        """returns if n is a Triangle Number"""
        return TriangleNumbers._isTriangleNumber(n) and Naturals.isNatural(n)

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
    def _isSquareNumber(n: Number) -> bool:
        """return if n passes the test unique to Square numbers
        but not classes it inherits from"""
        return SquareNumbers.inverseFormula(n) % 1 == 0

    @staticmethod
    def isSquareNumber(n: Number) -> bool:
        """returns if n is a Square Number"""
        return SquareNumbers._isSquareNumber(n) and Naturals.isNatural(n)

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
    def _isPentagonalNumber(n: Number) -> bool:
        """return if n passes the test unique to Pentagonal numbers
        but not classes it inherits from"""
        return PentagonalNumbers.inverseFormula(n) % 1 == 0

    @staticmethod
    def isPentagonalNumber(n: Number) -> bool:
        """returns if n is a Pentagonal Number"""
        return PentagonalNumbers._isPentagonalNumber(n) and Naturals.isNatural(n)

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
    def _isHexagonalNumber(n: Number) -> bool:
        """return if n passes the test unique to Hexagonal numbers
        but not classes it inherits from"""
        return HexagonalNumbers.inverseFormula(n) % 1 == 0

    @staticmethod
    def isHexagonalNumber(n: Number) -> bool:
        """returns if n is a Hexagonal Number"""
        return HexagonalNumbers._isHexagonalNumber(n) and Naturals.isNatural(n)

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
    def _isHeptagonalNumber(n: Number) -> bool:
        """return if n passes the test unique to Heptagonal numbers
        but not classes it inherits from"""
        return HeptagonalNumbers.inverseFormula(n) % 1 == 0

    @staticmethod
    def isHeptagonalNumber(n: Number) -> bool:
        """returns if n is a Heptagonal Number"""
        return HeptagonalNumbers._isHeptagonalNumber(n) and Naturals.isNatural(n)

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
    def _isOctagonalNumber(n: Number) -> bool:
        """return if n passes the test unique to Octagonal numbers
        but not classes it inherits from"""
        return OctagonalNumbers.inverseFormula(n) % 1 == 0

    @staticmethod
    def isOctagonalNumber(n: Number) -> bool:
        """returns if n is a Octagonal Number"""
        return OctagonalNumbers._isOctagonalNumber(n) and Naturals.isNatural(n)

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
