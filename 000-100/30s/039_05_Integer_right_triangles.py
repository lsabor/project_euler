"""
## Integer right triangles
Problem 39

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, 
there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?


Link: https://projecteuler.net/problem=39

Date solved:  
2022/07/06
"""

ANSWER = 840

# imports

from maths.primes import divisorCount

# solution


def solution():

    best = 1
    count = 0
    for i in range(1001):
        t = divisorCount(i)
        if t > count:
            count = t
            best = i
    return best


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution()
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
