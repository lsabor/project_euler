"""
## Prime digit replacements
Problem 51

By replacing the 1st digit of the 2-digit number *3, it turns out that 
six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 
5-digit number is the first example having seven primes among the ten 
generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 
56773, and 56993. Consequently 56003, being the first member of this family, 
is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not 
necessarily adjacent digits) with the same digit, is part of an eight 
prime value family.

Link: https://projecteuler.net/problem=51

Date solved:  
2022/07/24
"""

# TODO: refactor for speed

ANSWER = 121313

# imports

from maths.sequences import PrimesSeq
from maths.math import powerset
import re

# solution


def get_replacements(strint):
    replacements = set()
    for subset in powerset(range(len(strint) - 1)):
        if subset:
            replacement = list(strint)
            for index in subset:
                replacement[index] = "x"
            replacement = "".join(replacement)
            replacements.add(replacement)
    return replacements


def count_replacement_primes(rep_str, p_set):
    count = 0
    min_val = ""
    for i in range(10):
        p = re.sub("x", str(i), rep_str)
        if (p[0] != "0") and (int(p) in p_set):
            if not min_val:
                min_val = p
            count += 1
    return count, min_val


def largest_digit_replacement():
    P = PrimesSeq()
    ps = P.seq
    p_set = P.set()
    tested = set()

    largest = (0, 0)

    for p in ps:
        count = 0
        replacements = get_replacements(str(p))
        for rep in replacements:
            if rep not in tested:
                c, min_val = count_replacement_primes(rep, p_set)
                if c > count:
                    count = c
                    mv = min_val

        if count > largest[1]:
            largest = (int(mv), count)

        if largest[1] == 8:
            return largest[0]

        tested = tested.union(replacements)


def solution():

    return largest_digit_replacement()


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution()
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
