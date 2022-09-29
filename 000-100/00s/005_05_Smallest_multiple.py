"""
## Smallest multiple

Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


Link: https://projecteuler.net/problem=5

Date solved:  
2022/03/05
"""

ANSWER = 232792560

# imports

from maths.primes import lcm

# solution


def solution():
    return lcm(*range(2, 21))


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution()
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
