"""
## Circular primes
Problem 35

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

Link: https://projecteuler.net/problem=35

Date solved:  
2022/06/13
"""

ANSWER = 55

# imports

from maths.sequences import PrimesSeq

# solution
search_range = 1e6

P = PrimesSeq()
p = P.takeWhileLT(search_range)  # list of all the primes less than 1000000
p = set(p)  # turn into a set for much faster lookup


def is_circular(prime):
    p_strint = str(prime)
    # find the number of rotations that need to be checked
    # example: if p == 123, we need to only check 312 and 231
    cycles = len(p_strint) - 1
    for _ in range(cycles):
        p_strint = p_strint[1:] + p_strint[0]
        # check if our
        if int(p_strint) not in p:
            return False
    return True


def solution(bypass=False):
    if bypass:
        return ANSWER

    circular_prime_count = 0
    for prime in p:
        if is_circular(prime):
            circular_prime_count += 1

    return circular_prime_count


if __name__ == "__main__":
    solution(bypass=False)
