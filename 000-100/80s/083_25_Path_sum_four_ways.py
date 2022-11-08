"""
Path sum: four ways
Problem 83

NOTE: This problem is a significantly more challenging version of Problem 81.

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right,
by moving left, right, up, and down, is indicated in bold red [surrounded by underscores] and is equal to 2297.


[
    [_131_  673  _234_ _103_  _18_],
    [_201_  _96_ _342_  965  _150_],
    [ 630   803   746  _422_ _111_],
    [ 537   699   497  _121_  956 ],
    [ 805   732   524   _37_ _331_],
]

Find the minimal path sum from the top left to the bottom right by moving left, right,
up, and down in matrix.txt (right click and "Save Link/Target As..."), a 31K text file
containing an 80 by 80 matrix.

Link: https://projecteuler.net/problem=83

Date solved:  
11/08/2022
"""

ANSWER = 425185

# imports

from maths.parsing import auto_get_problem_file, read_file_as_array
from maths.graphs import *
import numpy as np

# solution

with open(auto_get_problem_file(), "r") as f:
    array = np.array(read_file_as_array(f))

# array = np.array(
#     [
#         [131, 673, 234, 103, 18],
#         [201, 96, 342, 965, 150],
#         [630, 803, 746, 422, 111],
#         [537, 699, 497, 121, 956],
#         [805, 732, 524, 37, 331],
#     ]
# )


def setup_graph(array):
    n = len(array)
    node_count = n**2 + 1

    nodes = np.array([])
    for i in range(node_count):
        nodes = np.append(nodes, Node(i))
    adjs = np.zeros((node_count, node_count, 2), dtype=int)
    adjs[-1][0] = [1, array[0][0]]
    for i, node in enumerate(nodes[:-1]):
        col = i % n  # column
        row = i // n  # row
        if row != n - 1:
            adjs[i, i + n] = [1, array[row + 1, col]]
            adjs[i + n, i] = [1, array[row, col]]
        if col != n - 1:
            adjs[i, i + 1] = [1, array[row, col + 1]]
            adjs[i + 1, i] = [1, array[row, col]]
    return Graph(nodes=nodes, adjs=adjs)


def solution():
    graph = setup_graph(array)
    dist, path = graph.lowest_cost_path(graph.nodes[-1], graph.nodes[-2])
    return int(dist)


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution()
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
