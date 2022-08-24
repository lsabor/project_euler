"""
## Ordered fractions
Problem 71

Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.

Link: https://projecteuler.net/problem=71

Date solved:  
2022/08/16
"""

ANSWER = 428570

# imports


# solution

# find fraction closest to, but less than 3/7
# we'll search for vals of n/d less than but closest to 3/7 for increasing vals of d
# if we search with increasing d, we don't have to worry about reducing the fraction to find n
# as that ratio will have already been tested

threshold = int(1e6)


def closest_ordered_fraction(threshold):
    target = 3 / 7
    ratio = target
    best_n = 0
    for d in range(1, threshold):
        n = int(target * d)
        new_fraction = n / d
        new_ratio = target - new_fraction
        if new_ratio < ratio and new_fraction != target:
            ratio = new_ratio
            best_n = n
    return best_n


def solution(bypass=True):
    if bypass:
        return ANSWER

    return closest_ordered_fraction(threshold)


if __name__ == "__main__":
    solution(bypass=False)
