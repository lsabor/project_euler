"""
## Digit factorials
Problem 34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.


Link: https://projecteuler.net/problem=34

Date solved:  
2022/06/13
"""

ANSWER = 40730

# imports

import itertools
from maths.math import factorial

# solution

f = [factorial(x) for x in range(10)]


def digit_factorial_iter(N):
    df_sum = 0
    for char in N:
        df_sum += f[int(char)]
    return df_sum


def solution():

    # find the number N such that n > digit_factorial(n) for n > N
    # N is a strint of 9's
    N = "9"
    while True:
        df = digit_factorial_iter(N)
        if df < int(N):
            break
        N += "9"

    # the maximum number of digitis is the length of N
    max_power = len(N)
    df_sum = 0

    # make all possible nums up to 7 digits long
    for possible in itertools.combinations_with_replacement(
        ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], r=max_power
    ):
        # we only care about digits, not order
        possible = sorted(possible)
        s = digit_factorial_iter(possible)
        # count the number of zeros, because we will add them in one by one checking to see
        # if any are a match for the digit factorial sum s
        zeros = possible.count("0")
        # our base case doesn't have any 0s - just the non-zero values
        s -= zeros
        for zero_count in range(zeros + 1):
            # add those zeros back in, see if any match our filter
            zero_extension = list("0" * zero_count) + possible[zeros:]
            n = s + zero_count  # add 1 back for each accepted 0
            num = sorted(list(str(n)))
            if num == zero_extension:
                df_sum += int(n)

    # the above filter includes 1! and 2! erroneously, so remove them manually
    df_sum -= 3
    return df_sum


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution()
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
