"""
## Largest prime factor

Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?



Link: https://projecteuler.net/problem=3

Date solved:  
2022/03/05
"""

ANSWER = 6857

# imports

from maths.primes import primeFactorization


# solution


def solution():
    n = 600851475143

    pf = primeFactorization(n)
    return max(pf)


if __name__ == "__main__":
    solution()
