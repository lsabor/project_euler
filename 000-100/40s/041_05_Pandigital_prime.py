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

"""
note:
any 9 digit pandigital number is divisible by 3: 9+8+7+6+5+4+3+2+1 = 45, thus never prime
same for 8 as 8+7+6+5+4+3+2+1 = 36
thus the largest number of digits a pandigital could be is 7
so start with 7654321
"""


def find_largest_pandigital():
    pandigital = "7654321"
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
    from time import perf_counter

    t0 = perf_counter()
    sol = solution(bypass=False)
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
