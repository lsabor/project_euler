"""
## Prime permutations
Problem 49

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?


Link: https://projecteuler.net/problem=49

Date solved:  
2022/07/24
"""

ANSWER = 296962999629

# imports

from maths.math import stringPermutations, permutations
from itertools import combinations_with_replacement
from maths.sequences import PrimesSeq

# solution

P = PrimesSeq()
ps = set(P.takeWhileLT(1e4))


def specials(nums: set):
    if len(nums) < 3:
        return None

    diffs = dict()
    for pair in permutations(nums, 2):
        a = min(pair)
        b = max(pair)
        diff = b - a
        if diff in diffs:
            diffs[b - a] = diffs[b - a].union(set(pair))
        else:
            diffs[b - a] = set(pair)

    for diff, vals in diffs.items():
        if len(diffs[diff]) == 3:
            return vals


def find_special_triplets():

    triplets = []

    for comb in combinations_with_replacement(
        ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], 4
    ):
        perms = map(int, stringPermutations(comb))
        nums = set([n for n in perms if ((n >= 1000) and (n in ps))])

        if triplet := specials(nums):
            triplets.append(triplet)

    return triplets


def new_triplet_concatenation(triplets):
    old_triplet = {1487, 4817, 8147}
    triplets.remove(old_triplet)

    concatenation = ""
    for n in triplets[0]:
        concatenation += str(n)

    return int(concatenation)


def solution(bypass=False):
    if bypass:
        return ANSWER

    return new_triplet_concatenation(find_special_triplets())


if __name__ == "__main__":
    solution(bypass=False)
