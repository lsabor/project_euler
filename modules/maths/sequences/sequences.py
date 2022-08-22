"""sequences"""


from io import TextIOWrapper
from typing import Iterable, Iterator
from xml.etree.ElementInclude import include
from maths.sets import *

import json
import os


cache_folder = os.path.join(os.path.dirname(__file__), "caches/")


def slicify(key: int | slice) -> slice:
    """returns key if slice else degenerate slice if key is int"""
    if isinstance(key, slice):
        return key
    elif isinstance(key, int):
        return slice(key, key + 1, 1)
    raise ValueError(f"{key=} must be a slice or int")


class Sequence(Set):
    """a set which is indexible, by default N0 in size"""

    name = "Sequence"
    example = "[s1 s2 s3 ...]"
    indexed = True
    cardinality = Cardinality("N0")
    local_caching = False
    first_value = ...
    monotonic = 0

    @log
    def __init__(self, seq: list[object] = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.comparitor = self.cardinality  # TODO this doesn't belong here
        self.seq = seq or ([self.first_value] if not self.first_value is ... else [])

        if self.cached:
            self.cache_file = cache_folder + self.name + ".json"
            cached_seq = self.readCache()
            self.seq = cached_seq or self.seq
            if not cached_seq:
                self.expandCache()

    def set(self):
        """returns self.seq as a set for easy lookup"""
        return set(self.seq)

    def _setupCache(self, action="x") -> TextIOWrapper:
        # simply generates the cache file if not already created
        if not os.path.exists(self.cache_file) and action not in ["w", "x"]:
            cache = open(self.cache_file, "x")
            cache.close()

    def _deserialize(self, cache: str) -> list[object]:
        """generic deserialization, overwrite for custom situations"""
        if data := cache.read():
            return json.loads(data)
        return []

    def _serialize(self, data: list[object] = None) -> str:
        """generic serialization, overwrite for custom situations"""
        if not data:
            data = self.seq
        return json.dumps(data)

    def readCache(self) -> list[object]:
        """entry point to read from cache"""
        self._setupCache("r")
        with open(self.cache_file, "r") as cache:
            deserialization = self._deserialize(cache)
        return deserialization

    def _overwriteCache(self, data: list[object] = None):
        """overwrites the serialization to the cache file"""
        self._setupCache("w")
        with open(self.cache_file, "w") as cache:
            cache.write(self._serialize(data))

    def concatenateCache(self, data: list[object]):
        """appends the serialization to the cache file"""
        raise NotImplementedError
        self._setupCache("a")
        with open(self.cache_file, "a") as cache:
            cache.write(self._serialize(data))

    def expandCache(self):
        """makes decision about how to expand the cache.
        Default is full overwrite"""
        self._overwriteCache()

    def destroyCache(self):
        """destroys Cache"""
        if os.path.exists(self.cache_file):
            os.remove(self.cache_file)

    def resetCache(self):
        """overwrites current Cache with nothing"""
        self.destroyCache()
        self._setupCache()

    def __getitem__(self, key: int | slice) -> Number | list[object]:
        return self.seq.__getitem__(key)

    def __iter__(self) -> Iterable[object]:
        self.i = 0
        return self

    def __next__(self) -> object:
        if self.i < len(self.seq) or self.cardinality.order:
            result = self[self.i]
            self.i += 1
            return result
        else:
            raise StopIteration

    def yieldWhile(self, include_condition, last_index=200000) -> Iterator[object]:
        # TODO change typing, Iterator[object] is not correct
        index = 0
        if not self.seq:
            raise ValueError(f"sequence is empty")
        iter_seq = iter(self)
        value = next(iter_seq)
        while include_condition(value):
            yield value
            value = next(iter_seq)

    def takeWhile(self, include_condition, last_index=200000, threshold=None) -> list:
        """takes values from seq until condition fails"""
        # TODO this needs some tweaking...
        direction = 1
        index = 0
        if (self.monotonic != 0) and (threshold is not None):
            # monotonic functions are easier to search, we can skip around
            if approxCount := getattr(self, "approxCount", None):
                # we have an appoximation algorithm about how many items to take
                index = approxCount(threshold)
                if index > last_index:
                    raise ValueError(f"condition always satisifed before {last_index=}")
                if not include_condition(self[index], threshold):
                    direction = -1
            else:
                # TODO: make this algorithm faster by jumping half distances until range == 2
                while include_condition(self[index], threshold):
                    index = 2 * index if index else 1
                    if index > last_index:
                        if index == 2 * last_index:
                            raise ValueError(
                                f"condition always satisifed before {last_index=}"
                            )
                        index = last_index
                index //= 2
        if direction:
            while include_condition(self[index], threshold):
                index += 1
        else:
            while not include_condition(self[index], threshold):
                index -= 1
            index += 1
        return self[:index]

    def takeWhileLT(self, n: float, last_index=200000) -> list:
        return self.takeWhile(lambda x, n: x < n, threshold=n, last_index=last_index)

    def takeWhileGT(self, n: float, last_index=200000) -> list:
        return self.takeWhile(lambda x, n: x > n, threshold=n, last_index=last_index)

    def takeWhileLE(self, n: float, last_index=200000) -> list:
        return self.takeWhile(lambda x, n: x <= n, threshold=n, last_index=last_index)

    def takeWhileGE(self, n: float, last_index=200000) -> list:
        return self.takeWhile(lambda x, n: x >= n, threshold=n, last_index=last_index)


class TestOnlySequence(Sequence):
    """a sequence where the nth element can only be computed by trying
    out values. Classes inheriting from this must have a set pull from
    and an method of generating the next possibility to test"""

    name = "TestOnlySequence"
    example = "PrimesSequence"
    local_caching = True

    @log
    def __init__(self, init_len: int = 0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.seq = self.seq if len(self.seq) > init_len else self[:init_len]

    def nextToTest(self, obj: object) -> object:
        ...

    def testUpTo(self, n: int):
        l = len(self.seq)
        if n < l:
            return
        current = self.seq[-1] if self.seq else self.first_value
        new_vals = []
        while l < n:
            current = self.nextToTest(current)
            while not self.isInSet(current):
                current = self.nextToTest(current)
            new_vals.append(current)
            l += 1
        self.seq += new_vals
        if self.cached:
            logger.debug(f" Extending cached seq of {self.name}")
            self.expandCache()

    def __getitem__(self, key):
        slicekey = slicify(key)
        if slicekey.stop > len(self.seq):
            logger.debug(
                f" Extending {'local' if not self.cached else ''} cache of {self.name}"
            )
            self.testUpTo(slicekey.stop)
            if self.cached:
                self.expandCache()
        return super().__getitem__(key)


class FormulaicSequence(Sequence):
    """a sequence where nth element can be computed directly from n
    must define formula method"""

    name = "FormulaicSequence"
    example = "[f(0) f(1) f(2) ...]"
    repr_len = 5

    @log
    def __init__(self, init_len: int = 1, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.seq = self.seq if len(self.seq) > init_len else self[:init_len]

    def formula(self, n: int) -> object:
        # TODO: implement grabbing from local cache first
        ...

    def __getitem__(self, key: int | slice) -> object | list[object]:
        slicekey = slicify(key)
        idxs = slicekey.indices(slicekey.stop)
        if idxs[0] == idxs[1] and isinstance(key, slice):
            return []
        if self.seq and slicekey.stop <= len(self.seq):
            return super().__getitem__(key)
        elif self.local_caching or self.cached:
            self.seq = self[: idxs[0]] + [self.formula(i) for i in range(*idxs[:2])]
            if self.cached:
                self.expandCache()
            return super().__getitem__(key)
        else:
            result = [self.formula(i) for i in range(*idxs)]
            return (
                result
                if (len(result) > 1) or isinstance(key, slice)
                else next(iter(result), None)
            )


class InvertableSequence(FormulaicSequence):
    """a sequence where nth element can be computed directly from n and vice versa
    must define inverseFormula and formula methods"""

    name = "InvertableFormulaicSequence"
    example = "[f(0) f(1) f(2) ...] where f: N <-> X"

    def inverseFormula(self, n: object) -> int:
        ...

    def _isInSetSpecified(self, n: object) -> bool:
        index = self.inverseFormula(n)
        return (index is not None) and ((index % 1) == 0)

    def getIndex(self, n: object) -> int:
        """gets the index of n"""
        self.test(n)
        return self.inverseFormula(n)

    def getNext(self, n: object) -> object:
        """gets the succeeding value of n"""
        index = self.getIndex(n)
        return self.formula(index + 1)

    def getPrevious(self, n: object) -> object:
        """gets the succeeding value of n"""
        index = self.getIndex(n)
        if index == 0:
            raise ValueError(f"There is no predecessor to {n=} in {self.name}")
        return self.formula(index - 1)


class IterativeSequence(FormulaicSequence):
    """a sequence where nth element is computed from previous element(s)
    must define a getNext method"""

    name = "IterativeSequence"
    example = "[f(0) f(f(0)) f(f(f(0))) ...]"
    local_caching = True

    def getNext(self, n: object, *args, **kwargs) -> object:
        ...

    def formula(self, n: int) -> object:
        # TODO: implement grabbing from local cache first
        if n == 0:
            return self.first_value
        return self.getNext(self.formula(n - 1))


class InverseIterativeSequence(IterativeSequence, InvertableSequence):
    """a sequence where nth element is computer from previous element(s) and vice versa
    must define getNext and getPrevious methods"""

    name = "InverseIterativeSequence"
    example = "[f-1(f-1(0)) f-1(0) 0 f(0) ...]"

    def getPrevious(self, n: object) -> object:
        ...

    def inverseFormula(self, n: object) -> int:
        index = 0
        vals = [n]
        while n != self.first_value:
            index += 1
            n = self.getPrevious(n)
            vals.append(n)
        if self.local_caching and len(vals) > len(self.seq):
            self.seq = list(reversed(vals))
        return index
