"""This module holds basic sequence functions"""

from sequences.sequences import *
from sequences.special_sequences import *


# import json
# import os
# from collections import Counter


# cache_folder = os.path.join(os.path.dirname(__file__), "caches/")


# class Sequence:
#     display_len = 10

#     def __init__(self, n: int, threshold=100, *args, **kwargs):
#         self.threshold = threshold
#         self.cache_file = cache_folder + self.name + ".json"
#         self.read_cache()
#         if len(self.seq) < n:
#             self.extend_seq(n - len(self.seq))

#     def __repr__(self):
#         if len(self) < Sequence.display_len:
#             return str(self.seq)
#         return str(self.seq[: Sequence.display_len])

#     def __getitem__(self, key):
#         length = len(self.seq)
#         max = key.stop if isinstance(key, slice) else key
#         if max < length:
#             return self.seq[key]
#         else:
#             self.extend_seq(max - length + 1)
#             return self.seq[key]

#     def __len__(self):
#         return len(self.seq)

#     def reset(self):
#         # deletes cache (don't run this with primes please)
#         self.seq = self.starter_seq
#         self.update_cache()

#     def special_deserialize(self, seq):
#         return seq

#     def read_cache(self):
#         # initilizes self.seq
#         if os.path.exists(self.cache_file):
#             with open(self.cache_file, "r") as cache:
#                 self.seq = self.special_deserialize(json.load(cache))
#         else:
#             self.seq = self.starter_seq
#             self.update_cache()

#     def update_cache(self):
#         # saves current sequence in cache
#         with open(self.cache_file, "w") as cache:
#             cache.write(json.dumps(self.seq))

#     def display(self):
#         print(self.seq)

#     def nexts(self):
#         # gets the next values of seq from subclass func
#         return self.next_item_batch()

#     def add_items(self):
#         # appends next seq vals to current seq
#         nxts = self.nexts()
#         self.seq += nxts
#         if len(self) % self.threshold == 0 or len(nxts) > self.threshold:
#             self.update_cache()
#             print(f"{self.name} cache updated. New length = {len(self)}")
#         return nxts

#     def extend_seq(self, n: int):
#         # appends at least n values to current seq
#         while n > 0:
#             added = self.add_items()
#             n -= len(added)
#         return self

#     def take_while(self, include_condition, last_index=200000) -> list:
#         # takes values from seq until condition fails
#         passing = []
#         length = 0
#         while length < last_index:
#             new_item = self[length]
#             if include_condition(new_item):
#                 passing.append(new_item)
#                 length += 1
#             else:
#                 return passing
#         raise Exception(
#             f"Sequence {self.name} satisfies {include_condition} past last_index {last_index}"
#         )

#     def take_while_lt(self, n: float, last_index=200000) -> list:
#         return self.take_while(lambda x: x < n, last_index=last_index)

#     def take_while_gt(self, n: float, last_index=200000) -> list:
#         return self.take_while(lambda x: x > n, last_index=last_index)

#     def take_while_le(self, n: float, last_index=200000) -> list:
#         return self.take_while(lambda x: x <= n, last_index=last_index)

#     def take_while_ge(self, n: float, last_index=200000) -> list:
#         return self.take_while(lambda x: x >= n, last_index=last_index)


# class Primes(Sequence):
#     # lists the primes in sequential order
#     def __init__(self, n=1, *args, **kwargs):
#         self.name = "Primes"
#         self.starter_seq = [2]
#         super().__init__(n, *args, **kwargs)

#     def next_item(self):
#         # this is inefficient, just use next_item_batch
#         return self.next_item_batch[0]

#     def next_item_batch(self):
#         from primes import is_prime_single_check

#         current = self.seq[-1]
#         print(current)
#         to_check = list(range(current, current + self.threshold))[::2]
#         print(to_check)
#         primes = [n for n in to_check if is_prime_single_check(n)]
#         print(f"Adding primes between {primes[0]} and {primes[-1]}")
#         return primes

#     def reset(self):
#         raise Exception("Please don't reset the cache for primes")


# class Fibonacci(Sequence):
#     # lists the Fibonacci sequence in order
#     def __init__(self, n=2, *args, **kwargs):
#         self.name = "Fibonacci"
#         self.starter_seq = [1, 1]
#         super().__init__(n, *args, **kwargs)

#     def next_item(self):
#         return self.seq[-2] + self.seq[-1]

#     def next_item_batch(self):
#         return [self.next_item()]


# class Natural(Sequence):
#     # lists the natural numbers in order
#     def __init__(self, n=1, *args, **kwargs):
#         self.name = "Natural"
#         self.starter_seq = [1]
#         super().__init__(n, *args, **kwargs)

#     def next_item(self):
#         return self.seq[-1] + 1

#     def next_item_batch(self):
#         return [self.next_item()]


# class Triangle_Numbers(Sequence):
#     # lists the triangle numbers in order
#     # Nth triangle num is sum of all natural numbers up to N
#     def __init__(self, n=1, *args, **kwargs):
#         self.name = "Triangle_Numbers"
#         self.starter_seq = [1]
#         super().__init__(n, *args, **kwargs)

#     def next_item(self):
#         n = len(self.seq) + 1
#         return int(n * (n + 1) / 2)

#     def next_item_batch(self):
#         return [self.next_item()]


# class Pentagonal_Numbers(Sequence):
#     # lists the pentagonal numbers in order
#     def __init__(self, n=1, *args, **kwargs):
#         self.name = "Pentagonal_Numbers"
#         self.starter_seq = [1]
#         super().__init__(n, *args, **kwargs)

#     def next_item(self):
#         n = len(self.seq) + 1
#         return int(n * (3 * n - 1) / 2)

#     def next_item_batch(self):
#         return [self.next_item()]


# class Prime_Factorizations(Sequence):
#     """lists the prime factorizations in Counter form of the natural numbers in order"""

#     def __init__(self, n=1, *args, **kwargs):
#         self.name = "Prime_Factorizations"
#         self.starter_seq = [Counter()] * 2
#         super().__init__(n, *args, **kwargs)

#     def next_item(self):
#         # this is inefficient, just use next_item_batch
#         return self.next_item_batch[0]

#     def next_item_batch(self):
#         from primes import prime_factorization

#         return [prime_factorization(len(self) + n) for n in range(self.threshold)]

#     def reset(self):
#         raise Exception("Please don't reset the cache for Prime Factorizations")

#     def special_deserialize(self, seq):
#         return [Counter({int(k): v for k, v in d.items()}) for d in seq]


# class Problem0477_Numbers(Sequence):
#     # lists the Problem0477 numbers in order
#     def __init__(self, n=1, *args, **kwargs):
#         self.name = "Problem0477_Numbers"
#         self.starter_seq = [0]
#         super().__init__(n, *args, **kwargs)

#     def next_item(self):
#         return (self.seq[-1] ** 2 + 45) % 1000000007

#     def next_item_batch(self):
#         return [self.next_item()]


# from sequences.compound import *
