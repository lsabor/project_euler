"""
## Example Problem
Problem 0

Problem statement:  
Let a+b=5 and b+c=2 and a+c=6.  
What is a+b+c?

Link: https://www.wolframalpha.com/input?i=a%2Bb%3D5%2C+b%2Bc%3D2%2C+a%2Bc%3D6%2C+a%2Bb%2Bc

Date solved:  
2022/03/05 [YYYY/MM/DD]
"""

ANSWER = 6.5

# imports

# solution

# algebra
# a = 5 - b
# b = 2 - c
# a = 6 - c
#
# 5 - b       = 6 - c
# 5 - (2 - c) = 6 - c
# 3 + c       = 6 - c
# c + c       = 6 - 3
# 2*c         = 3
c = 3 / 2
b = 2 - c
a = 5 - b


def solution(bypass=False):
    if bypass:
        return ANSWER
    return a + b + c


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution(bypass=False)
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
