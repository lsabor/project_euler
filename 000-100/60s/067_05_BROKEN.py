"""
## Maximum path sum II

Problem 67

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)



Link: https://projecteuler.net/problem=67

Date solved:  
2022/04/02
"""

ANSWER = 7273

# imports

from maths.parsing import readArrayStr
from maths import graphs

# solution


def solution(bypass=True):
    if bypass:
        return ANSWER

    file_name = "problem_files/p067_triangle.txt"
    with open(file_name, "r") as f:
        triangle = f.read()

    array = readArrayStr(triangle)

    graph = graphs.Graph()

    # makes a graph with edges equal to length of numbers in triangle
    first_node = graphs.Node("FIRST_NODE")
    current_row = [first_node]
    for i, row in enumerate(array):
        if i + 1 < len(array):
            next_row = []
            for k in range(i + 2):
                next_row_node = graphs.Node(value=f"({i},{k})")
                next_row.append(next_row_node)
        else:
            final_node = graphs.Node(value="FINAL_NODE")
            next_row = [final_node]
        for j, edge_length in enumerate(row):
            current_node = current_row[j]
            next_node_1 = next_row[j] if i + 1 < len(array) else next_row[0]
            next_node_2 = next_row[j + 1] if i + 1 < len(array) else next_row[0]
            new_edge_1 = graphs.Edge(
                length=100 - edge_length, node0=current_node, node1=next_node_1
            )
            new_edge_2 = graphs.Edge(
                length=100 - edge_length, node0=current_node, node1=next_node_2
            )
            graph.addEdgeSet(set([new_edge_1, new_edge_2]))
        current_row = next_row

    # finds shortest path from top to bottom, edge_length = 100-number
    # TODO: takes 5 minutes, should be refactored
    inverse_path_len, path_nodes = graph.shortestPathDirectional(first_node, final_node)

    path_length = 0
    for i in range(len(path_nodes) - 1):
        genesis = path_nodes[i]
        destiny = path_nodes[i + 1]
        relevant_edges = [
            edge for edge in graph.edges if edge.doesDirectionallyConnectNodes(genesis, destiny)
        ]
        edge = min(relevant_edges, key=lambda x: x.length)
        real_length = round(-(edge.length - 100))
        path_length += real_length

    return path_length


if __name__ == "__main__":
    solution(bypass=False)
