"""
## Double-base palindromes
Problem 36

The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)


Link: https://projecteuler.net/problem=36

Date solved:  
2022/06/13
"""

ANSWER = 872187

# imports


# solution


def solution(bypass=True):
    if bypass:
        return ANSWER

    max_value = int(1e6)

    sum_db_palendromes = 0
    for n in range(max_value):
        decimal_strint = str(n)
        if decimal_strint == decimal_strint[::-1]:
            binary_strint = bin(n)[2:]
            if binary_strint == binary_strint[::-1]:
                sum_db_palendromes += n

    return sum_db_palendromes


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution(bypass=False)
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer =", ANSWER)
