"""
## Champernowne's constant
Problem 40

An irrational decimal fraction is created by concatenating the positive integers:

0.12345678910_1_112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1,000 × d10,000 × d100,000 × d1,000,000


Link: https://projecteuler.net/problem=40

Date solved:  
2022/07/06
"""

ANSWER = 210

# imports


# solution


def solution():
    length = 1e6

    constant = ""
    n = 1

    while len(constant) < length:
        constant += str(n)
        n += 1

    product = 1
    for i in range(6):
        char = constant[10 ** (i + 1) - 1]
        product *= int(char)

    return product


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution()
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
