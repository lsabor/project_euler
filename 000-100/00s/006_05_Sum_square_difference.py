"""
## Sum square difference
Problem 6

The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

Link: https://projecteuler.net/problem=6

Date solved:  
2022/03/05
"""

ANSWER = 25164150

# imports

from maths.math import sumConsecutiveInts, sumSquares

# solution


def solution(bypass=False):
    if bypass:
        return ANSWER
    nums = range(1, 101)

    square_of_sums = sumConsecutiveInts(100) ** 2
    sum_of_squares = sumSquares(nums)

    return square_of_sums - sum_of_squares


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution(bypass=False)
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
