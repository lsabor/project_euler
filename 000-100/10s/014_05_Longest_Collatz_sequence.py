"""
## Longest Collatz sequence

Problem 14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.


Link: https://projecteuler.net/problem=14

Date solved:  
2022/03/08

Co-solved with Andrew Roberts  
Github: @ajroberts0417
"""

ANSWER = 837799

# imports


# solution

# TODO: refactor for speed


def func(n):
    return n // 2 if n % 2 == 0 else 3 * n + 1


def solution(bypass=False):
    if bypass:
        return ANSWER
    threshold = int(1e6)
    count = 0
    val = 1

    for i in range(2, 1000000):
        c = 0
        n = i
        while n != 1:
            n = func(n)
            c += 1
        if c > count:
            count = c
            val = i

    return val


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution(bypass=False)
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
