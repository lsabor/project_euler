import numpy as np
from collections import Counter
from itertools import takewhile

from maths.math.maths import sqrt


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

    print(f"done with {len(all_primatives)} primatives")

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


print(seive(int(1.5e6)))
