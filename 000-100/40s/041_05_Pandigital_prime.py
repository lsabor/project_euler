"""
## Pandigital prime
Problem 41

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?



Link: https://projecteuler.net/problem=41

Date solved:  
2022/07/06
"""

# TODO: refactor for speed

ANSWER = 7652413

# imports

from maths.primes import isPrime
from maths.math import permutations
from functools import reduce
from operator import add

# solution
def find_largest_pandigital():
    pandigital = "987654321"
    while True:
        for n in permutations(pandigital):
            # permutations should list the numbers in strictly decending order
            p = int(reduce(add, n))
            # print(p)
            if isPrime(p):
                return p
        pandigital = pandigital[1:]


def solution(bypass=False):
    if bypass:
        return ANSWER
    return find_largest_pandigital()


if __name__ == "__main__":
    solution(bypass=False)
