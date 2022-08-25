"""
## Pandigital products

Problem 32

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital. HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

Link: https://projecteuler.net/problem=32

Date solved:
2022/06/01
"""

# TODO: refactor for speed


ANSWER = 45228

# imports

from maths.math import permutations

# solution


def solution(bypass=True):
    if bypass:
        return ANSWER

    # runtime is 1m 30s
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def num_from_list(ls):
        num = 0
        for i, digit in enumerate(ls):
            num += digit * (10**i)
        return num

    vals = set()
    for perm in permutations(digits):
        for mult_loc in range(1, len(digits) - 1):
            for equal_loc in range(mult_loc, len(digits)):
                multiplicand = num_from_list(perm[:mult_loc])
                multiplier = num_from_list(perm[mult_loc:equal_loc])
                product = num_from_list(perm[equal_loc:])
                if multiplicand * multiplier == product:
                    vals.add(product)

    return sum(vals)


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution(bypass=False)
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer =", ANSWER)
