"""
## Self powers
Problem 48

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.


Link: https://projecteuler.net/problem=48

Date solved:  
2022/07/24
"""

ANSWER = 9110846700

# imports

from maths.math import tetrate

# solution


def sum_consecutive_tetrations(n: int, mod: int = 0):
    result = 0
    for i in range(1, n + 1):
        result += tetrate(i, mod=mod)
    return result


def solution(bypass=False):
    if bypass:
        return ANSWER

    return sum_consecutive_tetrations(1000, int(1e10)) % int(1e10)


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution(bypass=False)
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer =", ANSWER)
