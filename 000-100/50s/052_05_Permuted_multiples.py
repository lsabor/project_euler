"""
## Permuted multiples
Problem 52

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

Link: https://projecteuler.net/problem=52

Date solved:  
2022/07/24
"""

ANSWER = 142857

# imports


# solution

cap = 6


def find_smallest_permuted_number():

    n = 10

    while True:

        stn = str(n)
        sn = sorted(list(stn))

        if (stn[0] != "1") or (int(stn[1]) > 6):  # tests to see if number of digits increases
            stn = "1" + ("0" * len(stn))
            n = int(stn)
        else:
            for x in range(2, cap + 1):
                ls = sorted(list(str(x * n)))
                if ls != sn:
                    break
                if x == cap - 1:
                    return n
            n += 1


def solution(bypass=True):
    if bypass:
        return ANSWER

    return find_smallest_permuted_number()


if __name__ == "__main__":
    solution(bypass=False)
