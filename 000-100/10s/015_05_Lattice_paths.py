"""
## Lattice paths

Problem 15

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

Link: https://projecteuler.net/problem=15

Date solved:  
2022/03/06

Co-solved with Andrew Roberts  
Github: @ajroberts0417
"""

ANSWER = 137846528820

# imports

from maths.math import nChoosek

# solution


def solution(bypass=False):
    if bypass:
        return ANSWER
    # in a square lattice path, to get from the top left to bottom right,
    # at each intersection you can choose to go down or right
    # thus, of the 40 moves you make, you have to choose
    # 20 of them to be right hand turns
    # hence, 40 choose 20 is the correct answer

    n = 40
    k = 20

    return nChoosek(n, k)


if __name__ == "__main__":
    solution(bypass=False)
