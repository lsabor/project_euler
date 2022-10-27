"""
## Amicable numbers

Problem 21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.


Link: https://projecteuler.net/problem=21

Date solved:  
2022/03/21
"""

from time import perf_counter

t0 = perf_counter()

ANSWER = 31626

# imports

from maths.sequences.compound import DivisorSeq

# solution

DS = DivisorSeq()

search_depth = int(1e4)


def divsum(n: int) -> int:
    return sum(DS.seq[n]) - n


def sumAmicableNums(search_depth):
    amisum = 0
    for n in range(2, search_depth):
        ds = divsum(n)
        if (ds < search_depth) and (ds != n) and (divsum(ds) == n):
            amisum += n
    return amisum


def solution():
    return sumAmicableNums(search_depth)


if __name__ == "__main__":

    sol = solution()
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
