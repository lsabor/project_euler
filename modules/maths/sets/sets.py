"""The class Set which is a mathematical set"""

import inspect
from numbers import Number
from maths.logs import *
from functools import partial


class Set:
    """A collection of things"""

    name = "Set"
    example = "A collection of literally anything"
    ordered = False
    indexed = False
    cardinality = None
    cyclic = False
    cached = False
    datatypes = [object]

    @log
    def __init__(self, *args, **kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def __gt__(self, other) -> bool:
        if not self.ordered:
            raise TypeError(f"{self.name} is not an ordered set")
        return self.comparitor > other.comparitor

    def __eq__(self, other) -> bool:
        if not self.ordered:
            raise TypeError(f"{self.name} is not an ordered set")
        return self.comparitor == other.comparitor

    def __repr__(self) -> str:
        return self.name

    def __bool__(self) -> bool:
        return bool(self.cardinality)

    def __len__(self) -> int:
        if not self.cardinality:
            return 0
        elif self.cardinality.order == 0:
            return self.cardinality.value
        else:
            raise TypeError(f"Sets of size {self.cardinality} do not have a length.")

    @log
    def isInSet(self, n: object) -> bool:
        """returns if n is a in the Set by testing the _isInSet methods for each class"""
        loglevel = "DEBUG"

        # first check for valid data type
        if not any(isinstance(n, dtype) for dtype in self.datatypes):
            level_map[loglevel](
                f"{n} (type: {type(n)}) not valid datatype for {self.name}"
            )
            return False

        # we will start with the highest parent class, and test each on the way down
        # this is because the most basic class tests are usually simplest and
        # the reasons for failing will be the most useful

        # first run though _isInSet from highest to lowest level
        # then same through _isInSetSpecified since Specified version is
        # definied above the set in question, but is most specific

        in_set = False

        for _inSetTestName in ["_isInSet", "_isInSetSpecified"]:
            for klass in self.__class__.__mro__[::-1]:
                if _isInSet := getattr(klass, _inSetTestName, None):
                    # make sure it doesn't get double run
                    if klass.__name__ in _isInSet.__qualname__:
                        if inspect.ismethod(_isInSet):
                            in_set = log(level=loglevel)(_isInSet)(n)
                        else:
                            in_set = log(level=loglevel)(_isInSet)(self, n)
                        if not in_set:
                            # log the reason for failure
                            if "Specified" in _inSetTestName:
                                level_map[loglevel](
                                    f"{n} fails {self.name}-specific test"
                                )
                            else:
                                level_map[loglevel](
                                    f"{n} not in {klass.name}, thus not in {self.name}"
                                )
                            return False
        return in_set

    @classmethod
    def getValue(self, n: Number | object) -> object:
        if type(n) == type(self):
            n = n.value
        return n

    def size(self) -> "Cardinality":
        """reports cardinality, similar to len but for sets"""
        return self.cardinality

    def test(self, n, **kwargs) -> None:
        """raises TypeError if not isInSet(n)"""
        if not self.isInSet(n, **kwargs):
            raise TypeError(f"{n} is not in {self.name}. E.g. {self.example}")


class Cardinalities(Set):
    """Cardinality given to a set. Cardinalities is a set itself of course.
    Includes the 1. natural numbers, 2. N which represents a finite,
    but computationally prohibitively large natural number, and 3. Alephs (N0 N1 ...)
     indicates the size of a set"""

    name = "Cardinalities"
    example = "[0 1 2 ... N N0 N1 N2 ...]"
    ordered = True
    datatypes = [str, int, float, Set]

    @classmethod
    def _isInSet(klass, n: int | str) -> bool:
        """return if n is a cardinality"""
        if isinstance(n, klass):
            return True
        if type(n) == str:
            if not n or n[0] != "N":
                return False
            if len(n) == 1:
                return True
            try:
                f = float(n[1:])
                return f.is_integer() and (f >= 0)
            except:
                return False
        else:
            f = float(n)
            return f.is_integer() and f >= 0

    def __gt__(self, other) -> bool:
        if not isinstance(other, type(self)):
            raise TypeError(f"{type(other)} cannot be compared to {type(self)}")
        if self.order != other.order:
            return self.order > other.order
        return self.value > other.value

    def __eq__(self, other) -> bool:
        if not isinstance(other, type(self)):
            raise TypeError(f"{type(other)} cannot be compared to {type(self)}")
        return (self.order == other.order) and (self.value == other.value)

    def __bool__(self) -> bool:
        return True


class Cardinality(Cardinalities):
    """A specific Cardinality"""

    name = "Cardinality"

    def __init__(self, cardinality: int | str, *args, **kwargs):
        """cardinality must be either an int or
        string begining with N ending in '' or a number"""
        assert self.isInSet(cardinality), f"FAILED {cardinality} not valid cardinality"
        if type(cardinality) == str:
            self.order = 1
            self.value = -1 if len(cardinality) == 1 else int(cardinality[1:])
        else:
            self.order = 0
            self.value = cardinality

    def __repr__(self) -> str:
        if getattr(self, "order", None) is None:
            return self.name
        string = "N" if self.order else ""
        val = self.value
        string += "" if (not val + 1) else str(val)
        return string

    def __bool__(self) -> bool:
        return self > Cardinality(0)
