"""
## Convergents of e

Problem 65

JUST GO LOOK AT THE LINK, too many formatting issues to type out here

The square root of 2 can be written as an infinite continued fraction.

The infinite continued fraction can be written, , indicates that 2 repeats ad infinitum. In a similar way,

.

It turns out that the sequence of partial values of continued fractions for square roots provide the best rational approximations. Let us consider the convergents for

.

Hence the sequence of the first ten convergents for

are:

What is most surprising is that the important mathematical constant,

.

The first ten terms in the sequence of convergents for e are:

The sum of digits in the numerator of the 10th convergent is

.

Find the sum of digits in the numerator of the 100th convergent of the continued fraction for
.

Link: https://projecteuler.net/problem=65

Date solved:  
2022/
"""

ANSWER = 272

# imports

from maths.math import factorial
from decimal import *

# solution

depth = 100
getcontext().prec = 500  # we need e to be extremely precise


def get_e(precision=100):
    e = Decimal("0")
    for i in range(precision):
        e += Decimal("1") / Decimal(f"{factorial(i)}")
    return e


def get_covergent_numerator(depth):
    As = []
    remainder = get_e()

    for _ in range(depth):
        a = int(remainder)
        As.append(a)
        remainder = Decimal(1 / (remainder - a))

    return As


def fraction_from_continued_fraction(fraclist):
    revfl = fraclist[::-1]

    def reduce(a, num, den):
        # returns new num & den from (a + 1/(num/den))
        new_num = den + a * num
        new_den = num
        return new_num, new_den

    num = revfl[0]
    den = 1
    for a in revfl[1:]:
        num, den = reduce(a, num, den)
    return num, den


def solution(bypass=False):
    if bypass:
        return ANSWER

    num, den = fraction_from_continued_fraction(get_covergent_numerator(depth))
    return sum(list(map(int, str(num))))


if __name__ == "__main__":
    solution(bypass=False)
