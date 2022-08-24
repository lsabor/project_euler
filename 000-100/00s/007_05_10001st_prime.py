"""
## 10001st prime
 
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?

Link: https://projecteuler.net/problem=7

Date solved:  
2022/03/05
"""

ANSWER = 104743

# imports

from maths.sequences import PrimesSeq

# solution


def solution(bypass=False):
    if bypass:
        return ANSWER
    P = PrimesSeq()
    return P[10000]


if __name__ == "__main__":
    solution(bypass=False)
