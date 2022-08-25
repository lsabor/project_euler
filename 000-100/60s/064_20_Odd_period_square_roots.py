"""
## Odd period square roots

JUST GO LOOK AT THE LINK, too many formatting issues to type out here

All square roots are periodic when written as continued fractions and can be written in the form:

For example, let us consider
If we continue we would get the following expansion:
The process can be summarised as follows:
It can be seen that the sequence is repeating. For conciseness, we use the notation
, to indicate that the block (1,3,1,8) repeats indefinitely.
The first ten continued fraction representations of (irrational) square roots are:
, period=
, period=
, period=
, period=
, period=
, period=
, period=
, period=
, period=
, period=Exactly four continued fractions, for
, have an odd period.
How many continued fractions for
have an odd period?

Link: https://projecteuler.net/problem=64

Date solved:  
2022/07/30
"""

# TODO: consider optomizing

ANSWER = 1322

# imports

from maths.math import sqrt


# solution

threshold = 10000


def findPeriodicity(n):
    s = sqrt(n)
    if s % 1 == 0:
        return 0

    log = []
    a = int(s // 1)
    B = int(n - a**2)
    A = a
    frac = 1 / (s - a)

    while [A, B] not in log:
        log.append([A, B])

        a_new = frac // 1
        A_new = a_new * B - A
        B_new = (n - A_new**2) / B
        frac_new = (s + A_new) / B_new

        a = int(a_new)
        A = int(A_new)
        B = int(B_new)
        frac = frac_new

    return len(log)


def countOddPeriodicities(threshold):
    count = 0
    for n in range(2, threshold + 1):
        count += findPeriodicity(n) % 2 != 0
    return count


def solution(bypass=True):
    if bypass:
        return ANSWER

    return countOddPeriodicities(threshold)


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution(bypass=False)
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
