"""basic sets"""


class Set:
    """A collection of things"""

    name = "Set"
    example = "A collection of literally anything"
    ordered = False
    indexed = False
    cardinality = None
    cyclic = False

    def __init__(self, *args, **kwargs):
        ...

    def __getitem__(self, index):
        if not self.indexed:
            raise TypeError(f"{self.name} is not an indexed set")
        if index % 1 != 0:
            raise ValueError(f"{index = } must be an int")
        if (index < self.first_index) and (not self.cyclic):
            raise ValueError(f"{index = } is not a cyclic set")
        return self.formula(index)

    def __gt__(self, other):
        if not self.ordered:
            raise TypeError(f"{self.name} is not an ordered set")
        return self.comparitor > other.comparitor

    def __eq__(self, other):
        if not self.ordered:
            raise TypeError(f"{self.name} is not an ordered set")
        return self.comparitor == other.comparitor

    def __repr__(self):
        return self.example

    @classmethod
    def isInSet(self, n):
        ...

    @classmethod
    def getValue(self, n):
        if type(n) == type(self):
            n = n.value
        return n

    def size(self):
        return self.cardinality

    def errString(self, value):
        return f"{value} is not a {self.name}. E.g. {self.example}"

    def test(self, n):
        if not self.isInSet(n):
            raise ValueError(self.errString(n))


class Cardinalities(Set):
    """Cardinality given to a set. Cardinalities is a set itself of course.
    includes the natural numbers and Alephs (N0 N1 ...)
    generally indicates the size of a set"""

    name = "Cardinalities"
    example = "[0 1 2 ... N0 N1 N2 ...]"
    ordered = True

    @classmethod
    def _isInSet(self, n: int or str) -> bool:
        """return if input is a cardinality"""
        if type(n) == type(self):
            return (self.order in [0, 1]) and (isinstance(self.value, int))
        if type(n) == str:
            if len(n) < 2:
                return False
            if n[0] != "N":
                return False
            try:
                int(n[1:])
                return True
            except:
                return False
        else:
            return float(n).is_integer()

    @classmethod
    def isInSet(self, n) -> bool:
        return self._isInSet(n)

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
        # super().__init__(self, *args, **kwargs)
        assert Cardinalities.isInSet(cardinality), self.errString(cardinality)
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cardinality = Cardinality("N0")
        self.comparitor = self.cardinality

    @classmethod
    def _isInSet(self, n) -> bool:
        """return if n passes the test unique to Ints
        but not classes it inherits from"""
        try:
            return float(n).is_integer()
        except:
            return False

    @classmethod
    def isInSet(self, n) -> bool:
        """returns if n is an Int"""
        return Ints._isInSet(n)


class Naturals(Ints):
    """Natural Numbers"""

    name = "Naturals"
    example = "[0 1 2 3 ...]"
    indexed = True

    @classmethod
    def _isInSet(self, n) -> bool:
        """return if n passes the test unique to Natural numbers
        but not classes it inherits from"""
        return n >= 0

    @classmethod
    def isInSet(self, n) -> bool:
        """returns if n is a Natural number"""
        return Naturals._isInSet(n) and Ints.isInSet(n)

    @staticmethod
    def formula(n):
        if (n < 0) or (n % 1 != 0):
            raise ValueError(f"{n=} must be a natrual number")
        return n

    def getIndex(self, n) -> int:
        """gets the index of n"""
        n = self.getValue(n)
        if n % 1 == 0:
            return int(n)
        raise ValueError(self.errString(n))

    @staticmethod
    def inverseFormula(n):
        return n
