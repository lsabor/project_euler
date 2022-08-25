"""
## Cubic permutations
Problem 62

The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.

Link: https://projecteuler.net/problem=62

Date solved:  
2022/07/29
"""

ANSWER = 127035954683

# imports

from collections import defaultdict

# solution

threshold = 5


def findPermutedCubes(threshold):

    n = 1
    counts = defaultdict(lambda: [0, []])
    while True:
        new_cube = n**3
        strint = "".join(sorted(str(new_cube)))
        counts[strint][0] += 1
        counts[strint][1] = counts[strint][1] or new_cube
        if counts[strint][0] == threshold:
            return counts[strint][1]
        n += 1


def solution(bypass=True):
    if bypass:
        return ANSWER

    return findPermutedCubes(threshold)


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution(bypass=False)
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer =", ANSWER)
