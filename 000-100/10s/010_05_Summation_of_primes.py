"""
## Summation of primes

Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Link: https://projecteuler.net/problem=10

Date solved:  
2022/03/05
"""

ANSWER = 142913828922

# imports

from maths.sequences import PrimesSeq


# solution


def solution():
    P = PrimesSeq()
    cap = 2e6

    primes = P.takeWhileLT(cap)

    return sum(primes)


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution()
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
