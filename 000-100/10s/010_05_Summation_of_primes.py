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


def solution(bypass=False):
    if bypass:
        return ANSWER
    cap = 2e6

    P = PrimesSeq()
    primes = P.takeWhileLT(cap)

    return sum(primes)


if __name__ == "__main__":
    solution(bypass=False)
