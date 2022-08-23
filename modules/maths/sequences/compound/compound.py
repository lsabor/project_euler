"""sequences that are a bit unusual"""

from collections import Counter
import json

from maths.sets import PrimeFactorizations
from maths.primes import (
    primeFactorization,
    numFromCounter,
    divisors,
    lcm,
)
from maths.sequences import InvertableSequence


prefix = "compound/"


class PrimeFactorSeq(PrimeFactorizations, InvertableSequence):
    """Prime Factorizations as a sequence"""

    name = prefix + "PrimeFactorSequence"
    example = "[Counter({}) Counter({2:1}) Counter({3:1}) ...]"
    first_value = Counter()
    cached = True

    @staticmethod
    def formula(n: int) -> Counter:
        """returns the prime factorization of n"""
        return primeFactorization(n)

    @staticmethod
    def inverseFormula(n: Counter) -> int:
        """returns the index of the primeFactorization"""
        return numFromCounter(n)

    def _counterize_dict(self, entry):
        return Counter({int(key): value for key, value in entry.items()})

    def _deserialize(self, cache: str) -> list[object]:
        """generic deserialization, overwrite for custom situations"""
        if data := cache.read():
            loaded_data = json.loads(data)
            return list(map(self._counterize_dict, loaded_data))
        return []

    def _serialize(self, data: list[object] = None) -> str:
        """generic serialization, overwrite for custom situations"""
        if not data:
            data = self.seq
        return json.dumps(data)


class DivisorSeq(InvertableSequence):
    """Divisors as a sequence"""

    name = prefix + "DivisorSequence"
    example = "[[] [1] [1, 2] [1, 3] [1, 2, 4]...]"
    first_value = []
    cached = True
    PFS = PrimeFactorSeq()
    datatypes = [list]

    @classmethod
    def formula(klass, n: int) -> list[int]:
        """returns the list of divisors of n"""
        return divisors(n)

    @staticmethod
    def inverseFormula(n: list[int]) -> int:
        """returns n from a list of divisors"""
        return lcm(*n)

    @classmethod
    def _isInSet(klass, n: list[int]) -> bool:
        """returns if a list of ints is infact a complete divisor list"""
        return klass.formula(klass.inverseFormula(n)) == n


# class Divisors_Positive_Integers(sequences.Sequence):
#     # lists the Divisors in list form of the natural numbers in order
#     def __init__(self, n=1):
#         self.name = prefix + "Divisors_Positive_Integers"
#         self.starter_seq = [[0], [1]]
#         super().__init__(n)

#     def next_item(self):
#         return self.next_item_batch[0]

#     def next_item_batch(self):
#         length = len(self)
#         next_items = []
#         PF = sequences.Prime_Factorizations()
#         for i in range(length, length * 2 + 1):
#             next_items.append(divisors_from_pf_counter(PF[i]))
#         return next_items


# class Proper_Divisor_Sum_Positive_Integers(sequences.Sequence):
#     # lists the sum of the divisors of the natural numbers in order
#     def __init__(self, n=1):
#         self.name = prefix + "Proper_Divisor_Sum_Positive_Integers"
#         self.starter_seq = [0, 0]
#         super().__init__(n)

#     def next_item(self):
#         return sum(Divisors_Positive_Integers()[len(self)][:-1])

#     def next_item_batch(self):
#         return [self.next_item()]

#     def next_item(self):
#         return self.next_item_batch[0]

#     def next_item_batch(self):
#         length = len(self)
#         next_items = []
#         D = Divisors_Positive_Integers()
#         for i in range(length, length * 2 + 1):
#             next_items.append(sum(D[i][:-1]))
#         return next_items
