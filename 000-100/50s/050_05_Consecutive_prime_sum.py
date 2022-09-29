"""
## Consecutive prime sum
Problem 50

The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

Link: https://projecteuler.net/problem=50

Date solved:  
2022/07/24
"""

ANSWER = 997651

# imports

from maths.sequences import PrimesSeq

# solution

threshold = 1e6


def find_biggest_prime(threshold):
    P = PrimesSeq()
    ps = P.takeWhileLT(threshold)
    p_set = set(ps)  # makes searching much faster # TODO: refactor

    biggest_prime = [2, 1]
    # records the prime with the largest consecutive prime sum
    # [largest prime, # of consecutive primes that sum to it]

    for index, prime in enumerate(ps):
        summation = prime
        for j in range(index + 1, len(ps)):
            summation += ps[j]
            # test each consecutive sum
            if summation >= threshold:
                # no reason to continue on from here
                break
            if summation in p_set:
                count = (j + 1) - index  # the number of summed consecutive primes
                if count > biggest_prime[1]:
                    biggest_prime = [summation, count]

    return biggest_prime[0]


def solution():

    return find_biggest_prime(threshold)


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution()
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
