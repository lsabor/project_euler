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

# TODO: refactor for speed

ANSWER = 40730

# imports

from maths.math import factorial

# solution


def digit_factorial(N):
    df_sum = 0
    for char in str(N):
        df_sum += factorial(int(char))
    return df_sum


def solution(bypass=True):
    if bypass:
        return ANSWER

    # find the number N such that n > digit_factorial(n) for n > N
    # N is a strint of 9's
    N = "9"
    while True:
        df = digit_factorial(int(N))
        if df < int(N):
            break
        N = N + "9"

    # the maximum value is equal to the digit_factorial of N
    max_value = digit_factorial(int(N)) + 1

    # add all cases n <= max_value such that n == digit_facrorial(n)
    df_sum = 0
    for n in range(3, max_value):
        if n == digit_factorial(n):
            df_sum += n

    return df_sum


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution(bypass=False)
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer =", ANSWER)
