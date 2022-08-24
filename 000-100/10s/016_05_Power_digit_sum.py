"""
## Power digit sum

Problem 16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

Link: https://projecteuler.net/problem=16

Date solved:  
2022/03/06

Co-solved with Andrew Roberts  
Github: @ajroberts0417
"""

ANSWER = 1366

# imports


# solution


def solution(bypass=True):
    if bypass:
        return ANSWER
    n = 2**1000
    s = 0
    for char in str(n):
        s += int(char)
    return s


if __name__ == "__main__":
    solution(bypass=False)
