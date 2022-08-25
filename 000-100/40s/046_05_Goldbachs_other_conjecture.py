"""
## Goldbach's other conjecture
Problem 46

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
  
9 = 7 + 2×12  
15 = 7 + 2×22  
21 = 3 + 2×32  
25 = 7 + 2×32  
27 = 19 + 2×22  
33 = 31 + 2×12  

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?



Link: https://projecteuler.net/problem=46

Date solved:  
2022/07/10
"""

ANSWER = 5777

# imports

from maths.sequences import PrimesSeq
from maths.math import sqrt

# solution

P = PrimesSeq()
Ps = P.set()


def find_first_counterexample():
    n = 35  # lowest unchecked odd composite number
    possible = True
    while possible:
        possible = False
        if n in Ps:
            possible = True
            n += 2
        else:
            for p in P.takeWhileLT(n):
                m = sqrt((n - p) / 2)
                if m % 1 == 0:
                    possible = True
                    break
            n += 2
    return n - 2


def solution(bypass=False):
    if bypass:
        return ANSWER

    return find_first_counterexample()


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution(bypass=False)
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer =", ANSWER)
