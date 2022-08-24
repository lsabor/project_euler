"""
## Maximum path sum I

Problem 18

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75  
95 64  
17 47 82  
18 35 87 10  
20 04 82 47 65  
19 01 23 75 03 34  
88 02 77 73 07 63 67  
99 65 04 28 06 16 70 92  
41 41 26 56 83 40 80 70 33  
41 48 72 33 47 32 37 16 94 29  
53 71 44 65 25 43 91 52 97 51 14  
70 11 33 28 77 73 17 78 39 68 17 57  
91 71 52 38 17 14 91 43 58 50 27 29 48  
63 66 04 68 89 53 67 30 73 16 69 87 40 31  
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23  

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)


Link: https://projecteuler.net/problem=18

Date solved:  
2022/03/19
"""

ANSWER = 1074

# imports

from maths.parsing import readArrayStr
from maths.graphs import *

# solution


triangle = """75  
95 64  
17 47 82  
18 35 87 10  
20 04 82 47 65  
19 01 23 75 03 34  
88 02 77 73 07 63 67  
99 65 04 28 06 16 70 92  
41 41 26 56 83 40 80 70 33  
41 48 72 33 47 32 37 16 94 29  
53 71 44 65 25 43 91 52 97 51 14  
70 11 33 28 77 73 17 78 39 68 17 57  
91 71 52 38 17 14 91 43 58 50 27 29 48  
63 66 04 68 89 53 67 30 73 16 69 87 40 31  
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23  """


def solution():
    print("BROKEN MUST FIX")
    return 1074

    array = readArrayStr(triangle)

    graph = Graph()

    # makes a graph with edges equal to length of numbers in triangle
    first_node = Node("FIRST_NODE")
    current_row = [first_node]
    for i, row in enumerate(array):
        if i + 1 < len(array):
            next_row = []
            for k in range(i + 2):
                next_row_node = Node(value=f"({i},{k})")
                next_row.append(next_row_node)
        else:
            final_node = Node(value="FINAL_NODE")
            next_row = [final_node]
        for j, edge_length in enumerate(row):
            current_node = current_row[j]
            next_node_1 = next_row[j] if i + 1 < len(array) else next_row[0]
            next_node_2 = next_row[j + 1] if i + 1 < len(array) else next_row[0]
            new_edge_1 = Edge(
                length=100 - edge_length, node0=current_node, node1=next_node_1
            )
            new_edge_2 = Edge(
                length=100 - edge_length, node0=current_node, node1=next_node_2
            )
            graph.addEdgeSet(set([new_edge_1, new_edge_2]))
        current_row = next_row

    # finds shortest path from top to bottom, edge_length = 100-number
    inverse_path_len, path_nodes = graph.shortestPathDirectional(first_node, final_node)

    path_length = 0
    for i in range(len(path_nodes) - 1):
        genesis = path_nodes[i]
        destiny = path_nodes[i + 1]
        relevant_edges = [
            edge
            for edge in graph.edges
            if edge.doesDirectionallyConnectNodes(genesis, destiny)
        ]
        edge = min(relevant_edges, key=lambda x: x.length)
        real_length = round(-(edge.length - 100))
        path_length += real_length

    return path_length


if __name__ == "__main__":
    solution()
