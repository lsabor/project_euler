"""
## Special Pythagorean triplet
 
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.


Link: https://projecteuler.net/problem=9

Date solved:  
2022/03/05
"""

ANSWER = 31875000

# imports

from maths.math import iterableProduct

# solution


def isPythagoreanTriple(a, b, c):
    return a**2 + b**2 == c**2


def findPythagorean(n):
    """we are going to search efficiently so that we never double test any numbers
    a+b<c
    and 2*c < 1000"""
    a = 1
    b = 2
    c = n - b - a
    while n // 3 < c:
        while a < b:
            if isPythagoreanTriple(a, b, c):
                return a * b * c
            a += 1
            b -= 1
        a = 1
        c -= 1
        b = n - c - a


def solution():
    return findPythagorean(1000)


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution()
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
