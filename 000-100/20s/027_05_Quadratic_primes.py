"""
## Quadratic primes
Problem 27

Euler discovered the remarkable quadratic formula:

n^^2+n+41

It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39>. However, when n=40, 40^^2 + 40 + 41 = 40(40+1) + 41 is divisible by 41, and certainly when n = 41, 41^^2 + 41 + 41 is clearly divisible by 41.

The incredible formula n^^2 -79*n + 1601 was discovered, which produces 80 primes for the consecutive values 0 <= n <= 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form: n^^2+ a*n + b, where |a| < 1000 and |b| <= 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.

Link: https://projecteuler.net/problem=27

Date solved:  
2022/04/23
"""

# TODO: refactor for speed

ANSWER = -59231

# imports

from maths.sequences import PrimesSeq
from maths.math import product

# solution


def solution(bypass=False):
    if bypass:
        return ANSWER

    search = 1000

    P = PrimesSeq().set()

    def f(n, a, b):
        return n**2 + a * n + b

    ab = 0
    consecutive = 0
    for a, b in product(range(-search, search), range(-(search + 1), search + 1)):
        n = 0
        while f(n, a, b) in P:
            n += 1
        if n > consecutive:
            consecutive = n
            ab = a * b

    return ab


if __name__ == "__main__":
    solution(bypass=False)
