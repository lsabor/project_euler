"""
Path sum: two ways
Problem 81

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, 
by only moving to the right and down, is indicated in bold red [surrounded by underscores]
and is equal to 2427.

[
    [_131_  673   234   103    18 ],
    [_201_  _96_ _342_  965   150 ],
    [ 630   803  _746_ _422_  111 ],
    [ 537   699   497  _121_  956 ],
    [ 805   732   524   _37_ _331_],
]

Find the minimal path sum from the top left to the bottom right by only moving right
and down in matrix.txt (right click and "Save Link/Target As..."), a 31K text file 
containing an 80 by 80 matrix.

Link: https://projecteuler.net/problem=81

Date solved:  
10/28/2022
"""

ANSWER = 427337

# imports

from maths.parsing import auto_get_problem_file, read_file_as_array
from maths.graphs import *
import numpy as np

# solution

with open(auto_get_problem_file(), "r") as f:
    array = np.array(read_file_as_array(f))


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
        if col != n - 1:
            adjs[i, i + 1] = [1, array[row, col + 1]]

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
