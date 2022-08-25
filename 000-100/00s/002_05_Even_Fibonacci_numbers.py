"""
## Even Fibonacci numbers 

Problem 2

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

Link: https://projecteuler.net/problem=2

Date solved:  
2022/03/05
"""

ANSWER = 4613732

# imports

from maths.sequences import Fibonacci


# solution


def solution(bypass=False):
    if bypass:
        return ANSWER
    max_val = 4e6

    F = Fibonacci()
    summation = 0
    for n in F:
        if n % 2 == 0:
            summation += n
        if n > max_val:
            break

    return summation


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution(bypass=False)
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
