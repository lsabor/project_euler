"""
Path sum: three ways
Problem 82

NOTE: This problem is a more challenging version of Problem 81.

The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left 
column and finishing in any cell in the right column, and only moving up, down, and 
right, is indicated in red and bold [surrounded by underscores]; the sum is equal to 994.


[
    [ 131   673  _234_ _103_  _18_],
    [_201_  _96_ _342_  965   150 ],
    [ 630   803   746   422   111 ],
    [ 537   699   497   121   956 ],
    [ 805   732   524    37   331 ],
]

Find the minimal path sum from the left column to the right column in matrix.txt 
(right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.

Link: https://projecteuler.net/problem=82

Date solved:  
11/08/2022
"""

ANSWER = 260324

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
    for i in range(len(array)):
        # starting node is last node in list
        # and is set adjacent to all nodes in first row
        adjs[-1][len(array) * i] = [1, array[i][0]]
    for i, node in enumerate(nodes[:-1]):
        col = i % n  # column
        row = i // n  # row
        if row != n - 1:
            adjs[i, i + n] = [1, array[row + 1, col]]
            adjs[i + n, i] = [1, array[row, col]]
        if col != n - 1:
            adjs[i, i + 1] = [1, array[row, col + 1]]
    graph = Graph(nodes=nodes, adjs=adjs)
    # add terminal node
    last_node = Node(array.size + 1)
    last_adjs = [[0, 0]] * (array.size + 2)
    for i in range(0, array.size, len(array)):
        last_adjs[i + len(array) - 1] = [1, 0]
    graph.add_new_node(
        node=last_node,
        from_adjs=last_adjs,
    )
    return graph


def solution():
    graph = setup_graph(array)
    dist, path = graph.lowest_cost_path(graph.nodes[-2], graph.nodes[-1])
    return int(dist)


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution()
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
