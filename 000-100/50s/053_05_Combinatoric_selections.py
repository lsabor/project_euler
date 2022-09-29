"""
## Combinatoric selections
Problem 53

There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5_C_3 = 10

In general, n_C_r = n! / (r! * (n-r)!) and r <= n

It is not until n = 23, that a value exceeds one-million: 23_C_10 = 1144066

How many, not necessarily distinct, values of n_C_r for 1 <= n <= 100, are greater than one-million?

Link: https://projecteuler.net/problem=52

Date solved:  
2022/07/24
"""

ANSWER = 4075

# imports

from maths.math import nChoosek

# solution

threshold = int(1e6)


def find_big_comb_vals():
    count = 0

    for n in range(1, 101):
        for k in range(1, n + 1):
            nck = nChoosek(n, k)
            if nck > threshold:
                count += 1

    return count


def solution():

    return find_big_comb_vals()


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution()
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
