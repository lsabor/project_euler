"""
## Counting Sundays

Problem 19

You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?



Link: https://projecteuler.net/problem=19

Date solved:  
2022/03/21
"""

ANSWER = 31626

# imports

from maths.sequences.compound import DivisorSeq

# solution

DS = DivisorSeq()

search_depth = int(1e4)
DS[search_depth]  # makes sure DS gets populated up to search_depth


def divsum(n: int) -> int:
    return sum(DS.seq[n]) - n


def sumAmicableNums(search_depth):
    amisum = 0
    for n in range(2, search_depth):
        ds = divsum(n)
        if (ds < search_depth) and (ds != n) and (divsum(ds) == n):
            amisum += n
    return amisum


def solution(bypass=False):
    if bypass:
        return ANSWER
    return sumAmicableNums(search_depth)


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution(bypass=False)
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer =", ANSWER)
