"""
## Digit cancelling fractions
Problem 33

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.


Link: https://projecteuler.net/problem=33

Date solved:  
2022/06/07
"""

# TODO: refactor answer to generate 100

ANSWER = 100

# imports

from maths.math import product

# solution


def solution(bypass=False):
    if bypass:
        return ANSWER

    r = range(1, 10)
    # there can never be a zero anywhere

    reducibles = []
    for i, j, d in product(r, r, r):
        # cases
        # id / jd
        if i != j:
            num = 10 * i + d
            den = 10 * j + d
            if num / den == i / j and num / den < 1:
                reducibles.append(num / den)
                # reducibles.append([i,d,j,d])
        # id / dj
        if i != d or j != d:
            num = 10 * i + d
            den = 10 * d + j
            if num / den == i / j and num / den < 1:
                reducibles.append(num / den)
                # reducibles.append([i,d,d,j])
        # di / jd
        if i != d or j != d:
            num = 10 * d + i
            den = 10 * j + d
            if num / den == i / j and num / den < 1:
                reducibles.append(num / den)
                # reducibles.append([d,i,j,d])
        # di / dj
        if i != j:
            num = 10 * d + i
            den = 10 * d + j
            if num / den == i / j and num / den < 1:
                reducibles.append(num / den)
                # reducibles.append([d,i,d,j])

    assert reducibles == [0.25, 0.2, 0.4, 0.5]
    # 1/4 * 1/5 * 2/5 * 1/2
    # 2 / 200
    # 1 / 100
    return 100


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution(bypass=False)
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
