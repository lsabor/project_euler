"""
Square root digital expansion
Problem 80

It is well known that if the square root of a natural number is not an integer, 
then it is irrational. The decimal expansion of such square roots is infinite 
without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the 
first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of 
the first one hundred decimal digits for all the irrational square roots.

Link: https://projecteuler.net/problem=80

Date solved:  
09/30/2022
"""

ANSWER = 40886

# imports

from decimal import getcontext, Decimal

# solution

getcontext().prec = 102


def solution():
    total = 0
    for n in range(1, 101):
        n = Decimal(n)
        sr = n.sqrt()
        string = str(sr)
        if len(string) < 100:
            continue
        for digit in string[:101]:
            if digit != ".":
                total += int(digit)

    return total


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution()
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
