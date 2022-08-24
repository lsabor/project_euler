"""
## Diophantine equation
Problem 66

Consider quadratic Diophantine equations of the form:

x2 – Dy2 = 1

For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

3^2 – 2×2^2 = 1  
2^2 – 3×1^2 = 1  
9^2 – 5×4^2 = 1  
5^2 – 6×2^2 = 1  
8^2 – 7×3^2 = 1  

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.


Link: https://projecteuler.net/problem=66

Date solved:  
2022/
"""

ANSWER = 661

# imports

from maths.math import sqrt

# solution

threshold = 1000


def find_diophantine_solutions(threshold):
    # finding solutions using continued fractions

    biggest_D = 0
    biggest_x = 0

    for D in range(2, threshold + 1):
        limit = sqrt(D)
        if limit % 1 == 0:
            continue
        limit = int(limit)

        m = 0
        d = 1
        a = limit

        x1 = 1
        x = a

        y1 = 0
        y = 1

        while ((x**2) - (D * (y**2))) != 1:
            m = d * a - m
            d = int((D - m**2) / d)
            a = int((limit + m) / d)

            x2 = x1
            x1 = x
            y2 = y1
            y1 = y

            x = a * x1 + x2
            y = a * y1 + y2

        if x > biggest_x:
            biggest_x = x
            biggest_D = D

    return biggest_D


def solution(bypass=True):
    if bypass:
        return ANSWER

    return find_diophantine_solutions(threshold)


if __name__ == "__main__":
    solution(bypass=False)
