"""
## Singular integer right triangles
Problem 75

It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided 
right angle triangle in exactly one way, but there are many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right 
angle triangle, and other lengths allow more than one solution to be found; for example, using 
120 cm it is possible to form exactly three different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one 
integer sided right angle triangle be formed?

Link: https://projecteuler.net/problem=75

Date solved:  
2022/09/05
"""

# TODO: refactor for speed

ANSWER = 161667

# imports

import numpy as np

# solution


def generate_primatives(max_p):
    """generates all pythagorean with perimeter less than max_p"""

    primatives = [np.array([[3, 4, 5]])]
    first_primative = primatives[0]

    U = np.array([[1, 2, 2], [-2, -1, -2], [2, 2, 3]])
    A = np.array([[1, 2, 2], [2, 1, 2], [2, 2, 3]])
    D = np.array([[-1, -2, -2], [2, 1, 2], [2, 2, 3]])

    def next_primatives(prim):
        return (np.dot(prim, mat) for mat in (U, A, D))

    def recurse(prim):
        prims = (prim,)
        for p in next_primatives(prim):
            if np.sum(p) < max_p:
                prims += recurse(p)
        return prims

    return recurse(first_primative)


def seive(max_p):
    """seives in perimeters if they are found once,
    and then out perminently if found again"""

    all_primatives = generate_primatives(max_p)

    perimeters = list(np.sum(triplet) for triplet in all_primatives)
    perimeters.sort()

    result = 0
    triangles = [0] * (max_p + 1)

    for perim in perimeters:
        for p in range(perim, max_p + 1, perim):
            triangles[p] += 1
            if triangles[p] == 1:
                result += 1
            elif triangles[p] == 2:
                result -= 1

    return result


def solution():

    return seive(int(1.5e6))


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution()
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
