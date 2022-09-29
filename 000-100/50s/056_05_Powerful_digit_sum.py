"""
## Powerful digit sum
Problem 56

A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?

Link: https://projecteuler.net/problem=56

Date solved:  
2022/07/25
"""

ANSWER = 972

# imports

from maths.math import product

# solution

cap = 100


def find_powerful_digit_sum():
    max_sum = 0
    for a, b in product(range(1, cap), range(1, cap)):
        val = 0
        strint = str(a**b)
        for char in strint:
            val += int(char)
        max_sum = max(max_sum, val)

    return max_sum


def solution():

    return find_powerful_digit_sum()


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution()
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
