"""
## Sub-string divisibility
Problem 43

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.



Link: https://projecteuler.net/problem=43

Date solved:  
2022/07/07
"""

# TODO: refactor for speed


ANSWER = 16695334890

# imports

from maths.math import isDivisible, stringPermutations

# solution

primes = [2, 3, 5, 7, 11, 13, 17]

max_pandigital = "9876543210"  # we will have to remove any with leading 0


def has_sub_string_divisibility(strint: str) -> bool:
    for index, p in enumerate(primes):
        i = index + 1
        n = int(strint[i : i + 3])
        if not isDivisible(n, p):
            return False
    return True


def get_all_pandigital_with_ssd():
    pwssd = []
    for pandigital in stringPermutations(max_pandigital):
        n = int(pandigital)
        if n > 1e9:  # filters out pandigitals with leading 0's
            if has_sub_string_divisibility(pandigital):
                pwssd.append(n)
    return pwssd


def solution(bypass=False):
    if bypass:
        return ANSWER

    return sum(get_all_pandigital_with_ssd())


if __name__ == "__main__":
    solution(bypass=False)
