"""
## Square root convergents
Problem 57

It is possible to show that the square root of two can be expressed as an infinite continued fraction.

sqrt(2) = 1 + (1 / (2 + 1/ (2+1/(2+1/ ... ))))

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1 / (2 + 1/2) = 7/5 = 1.4
1 + 1 / (2 + 1/(2+ 1/2)) = 18/12 = 1.4166
next = 41/29 = 1.41379

The next three expansions are
99/70, 239/169, 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?

Link: https://projecteuler.net/problem=57

Date solved:  
2022/07/25
"""

ANSWER = 153

# imports

from maths.math import product

# solution

threshold = 1000


def count_disproportionate_convergents():
    count = 0

    for i in range(threshold):
        a = 2
        b = 1
        # do the 2- 1/(a/b) thing a bunch
        while i > 0:
            temp = a
            a = 2 * a + b
            b = temp
            i -= 1

        final_numerator = a + b
        final_denomerator = a

        count += len(str(final_numerator)) > len(str(final_denomerator))

    return count


def solution():

    return count_disproportionate_convergents()


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution()
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
