"""
## Digit factorial chains
Problem 74

The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145  

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169  
871 → 45361 → 871  
872 → 45362 → 872  

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)  
78 → 45360 → 871 → 45361 (→ 871)  
540 → 145 (→ 145)  

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?

Link: https://projecteuler.net/problem=73

Date solved:  
2022/08/17
"""

ANSWER = 0

# imports

from maths.math import factorial
from functools import lru_cache
import sys

print(sys.getrecursionlimit())

# solution

# for each n < 1e6,
factorials = [factorial(n) for n in range(10)]  # to avoid recomputing

threshold = int(1e6)


def digit_factorial_sum(n):
    return sum([factorials[int(char)] for char in str(n)])


def digit_factorial_chains(threshold, length):
    # loop_nums = set([0,1,2,145,169,363601,1454,871,872,45361,45362])
    loop_nums = set()

    # @lru_cache
    def chain_len(n):
        nonlocal loop_nums
        nonlocal seen
        nonlocal l
        if n in loop_nums:
            # print(f"{n=} found in {loop_nums=}")
            # print(f"total chain {seen}, {n}")
            return
        if n in seen:
            # print(f"{loop_nums=}")
            loop_nums = loop_nums.union(set(seen[seen.index(n) :]))
            # print(f"{loop_nums=}")
            # print(f"{n} loops in {seen}, so returning {seen.index(n) - len(seen)}")
            l -= seen.index(n) - len(seen)
            return
        seen.append(n)
        l += 1
        if l <= length:
            chain_len(digit_factorial_sum(n))
        return

    count = 0
    for n in range(0, threshold):
        seen = []
        l = 0
        # print()
        # print(f"{n=}")
        # print(f"{count=}")
        # print(f"{loop_nums=}")
        chain_length = chain_len(n)
        # print(f"{chain_length=}")
        count += l == length

    return count, loop_nums


def solution(bypass=True):
    if bypass:
        return ANSWER

    return digit_factorial_chains(threshold, 60)


if __name__ == "__main__":
    solution(bypass=False)
