"""
Counting summations
Problem 76

It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?

Link: https://projecteuler.net/problem=76

Date solved:  
2022/09/08
Solved with DeMehr Haywood
"""

# TODO: refactor for speed

ANSWER = 190569291

# imports

from functools import lru_cache

# solution


# @lru_cache
# def H(n, a):
#     if a == 1 or n == a:
#         print(n, a, 1)
#         return 1
#     if a > n:
#         print(n, a, 0)
#         return 0

#     end = min(a, n - a)

#     result = sum([H(n - a, b) for b in range(1, end + 1)])

#     print(n, a, result)

#     return result


# def f(n):
#     return sum([H(n, a) for a in range(1, n + 1)])


nmax = 100
ways = [1] + [0] * nmax
ways = [1]

div = 1
while True:
    for i in range()

for div in range(1,nmax):
    for i in range(len(ways)-div):
        ways[i + div] += ways[i]

print(ways[-1]) 

def solution(bypass=True):
    if bypass:
        return ANSWER
    # num = 10
    # return f(num) - 1

    nmax = 100
    ways = [1] + [0] * nmax
    for div in range(1, nmax):
        for i in range(len(ways) - div):
            ways[i + div] += ways[i]

    print(ways[-1])


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution(bypass=False)
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
