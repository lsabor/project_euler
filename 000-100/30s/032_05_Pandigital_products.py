"""
## Pandigital products

Problem 32

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to 
n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, 
multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written 
as a 1 through 9 pandigital. HINT: Some products can be obtained in more than one way so be 
sure to only include it once in your sum.

Link: https://projecteuler.net/problem=32

Date solved:
2022/06/01
"""


ANSWER = 45228

# imports

from re import L
from maths.math import permutations, sqrt

# solution


def solution():

    products = set()

    for mand_len in [1, 2]:  # multiplcand must be in range(2,100)
        for mand_tuple in permutations("123456789", mand_len):  # generate possible multiplicands
            mand_str = "".join(mand_tuple)
            mand = int(mand_str)
            max_mier = (
                10000 // mand
            )  # mand*mier=prod and sum of lens is 9, so mier is can't go above
            # this amount without increasing the length of the product too much
            remaining_digits = "123456789"
            for char in mand_str:
                remaining_digits.replace(char, "", 1)  # mier can't contain mand digits
            for mier_tuple in permutations(remaining_digits, 5 - mand_len):
                # len(mand) + len(mier) == 5
                mier_str = "".join(mier_tuple)
                mier = int(mier_str)
                if mier > max_mier:  # permutations go in ascending order
                    break
                prod = mand * mier
                prod_str = str(prod)
                if "0" in prod_str:
                    continue
                used_digits = set(mand_str + mier_str)
                unused_digits = set("123456789").difference(used_digits)
                if set(prod_str) == unused_digits:
                    products.add(prod)

    return sum(products)


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution()
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
