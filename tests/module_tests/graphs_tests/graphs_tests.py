"""tests for graphs"""

import string
import pytest

from maths.graphs.graphs import *


# class Test_Helpers:
#     """tests helper fxns in primes.py"""

#     @pytest.mark.parametrize(
#         "input,xoutput",
#         [
#             ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
#         ],
#     )
#     def test_nodify(self, output_or_error, input, xoutput):
#         output_or_error(
#             lambda x: [[node.value for node in row] for row in nodify(x)], input, xoutput
#         )


# @pytest.fixture
# def graph():
#     return Graph()


# @pytest.fixture
# def graph_with_nodes(graph):
#     n1 = Node(name="A", value=0)
#     n2 = Node(name="B", value=1)
#     graph.nodes = [n1, n2]
#     return graph


# @pytest.fixture
# def graph_unweighted(graph_with_nodes):
#     graph = graph_with_nodes
#     n1, n2 = graph.nodes
#     n1.add_adj(n2)
#     return graph


# @pytest.fixture
# def graph_weighted(graph_with_nodes):
#     graph = graph_with_nodes
#     graph.weighted = True
#     n1, n2 = graph.nodes
#     n1.add_adj(n2, 5)
#     return graph


# @pytest.fixture
# def graph_two_chains(graph):
#     for index, letter in enumerate(string.ascii_uppercase):
#         node = Node(value=index, name=letter)
#         graph.add_node(node)
#     count = len(graph.nodes)
#     for i in range(count - 1):
#         graph.add_edge(i, i + 1)
#     graph.remove_edge(count // 2 - 1, count // 2)

#     return graph


# class Test_Nodes:
#     """tests for the Node object"""

#     """
#     - nodes can have edges
#     - nodes can have unweighted or weighted edges
#     - edges can be removed from nodes
#     - get edges from a node
#     - edge can connect node to itself
#     """

#     @pytest.mark.current
#     def test_node_unweighted_adjs(self):
#         n1 = Node(1)
#         n2 = Node(2, adjs=[(n1, 1)])

#         assert n1.adjs == []
#         assert n2.adjs == [(n1, 1)]

#         n1.add_adj(n2)
#         assert n1.adjs == [(n2, 1)]

#     @pytest.mark.current
#     def test_node_weighted_adjs(self):
#         n1 = Node(1)
#         n2 = Node(2, adjs=[(n1, 5)])

#         assert n1.adjs == []
#         assert n2.adjs == [(n1, 5)]

#         n1.add_adj(n2, 7)
#         assert n1.adjs == [(n2, 7)]

#     @pytest.mark.current
#     def test_node_remove_unweighted_adj(self):
#         n1 = Node(1)
#         n2 = Node(2, adjs=[(n1, 1)])

#         n2.remove_adj(n1)
#         assert n2.adjs == []

#     @pytest.mark.current
#     def test_node_remove_weighted_adj_node_ref(self):
#         n1 = Node(1)
#         n2 = Node(2, adjs=[(n1, 5)])

#         n2.remove_adj(n1)
#         assert n2.adjs == []

#     @pytest.mark.current
#     def test_node_remove_weighted_adj(self):
#         n1 = Node(1)
#         n2 = Node(2, adjs=[(n1, 5)])

#         n2.remove_adj((n1, 5))
#         assert n2.adjs == []

#     @pytest.mark.current
#     def test_node_edge_to_itself(self):
#         node = Node()
#         node.add_adj(node, 2)
#         assert node.adjs == [(node, 2)]


# class Test_Graphs:
#     """tests for the Graph object"""

#     """
#     BASIC functionality:
#     - make a graph
#     - add some nodes
#     - add some edges
#     - remove nodes
#     - remove edges
#     - search for node with specific value
#     - search for node with edge with specific weight
#     - search for nodes that match condition
#     - get size of graph

#     RELATIONAL functionality like search, subgraphing, etc.
#     - return subgraph of connected nodes given some node as a graph
#     - return arbitrary subgraph from nodes w/o outside connections as a graph object
#     - find cliques of size
#     - find shortest path between nodes

#     """

#     @pytest.mark.current
#     def test_make_graph(self):
#         Graph()

#     @pytest.mark.current
#     def test_graph_with_nodes(self):
#         node = Node()
#         graph = Graph(nodes=[node])
#         assert graph.nodes == [node]

#     @pytest.mark.current
#     def test_graph_add_nodes(self, graph):
#         n1 = Node()
#         n2 = Node()
#         graph.add_node(n1)
#         graph.add_node(n2)
#         assert graph.nodes == [n1, n2]

#     @pytest.mark.current
#     def test_graph_remove_node(self, graph_with_nodes):
#         graph = graph_with_nodes
#         n1, n2 = graph.nodes
#         graph.remove_node(n1)
#         assert graph.nodes == [n2]
#         with pytest.raises(ValueError):
#             graph.remove_node(n1)

#     @pytest.mark.current
#     @pytest.mark.parametrize(
#         "n1_ref,n2_ref",
#         [
#             (0, 1),
#             ("A", "B"),
#             ("N1", "N2"),
#         ],
#     )
#     def test_graph_add_edge(self, graph_with_nodes, n1_ref, n2_ref):
#         graph = graph_with_nodes
#         n1, n2 = graph.nodes[:2]
#         if n1_ref == "N1":
#             n1_ref, n2_ref = n1, n2
#         graph.add_edge(n1_ref, n2_ref)
#         assert n1.adjs == [(n2, 1)]

#     @pytest.mark.current
#     def test_graph_remove_edge(self, graph_unweighted):
#         graph = graph_unweighted
#         n1, n2 = graph.nodes[:2]
#         graph.remove_edge(n1, n2)
#         assert n1.adjs == []

#     @pytest.mark.current
#     def test_graph_get_specific_node(self, graph_with_nodes):
#         graph = graph_with_nodes
#         node = graph.get_node((lambda node: node.name == "A"))
#         assert node.name == "A"

#     @pytest.mark.current
#     def test_graph_get_specific_node_by_name(self, graph_with_nodes):
#         graph = graph_with_nodes
#         node = graph.get_node_by_name("A")
#         assert node.name == "A"

#     @pytest.mark.current
#     def test_graph_get_specific_node_by_value(self, graph_with_nodes):
#         graph = graph_with_nodes
#         node = graph.get_node_by_value(0)
#         assert node.value == 0

#     @pytest.mark.current
#     def test_graph_get_node_by_edge_weight(self, graph_weighted):
#         graph = graph_weighted
#         node = graph.get_node(lambda node: any(adj[1] == 5 for adj in node.adjs))
#         assert node == graph.nodes[0]

#     @pytest.mark.current
#     def test_graph_get_nodes_by_condition(self, graph_with_nodes):
#         graph = graph_with_nodes
#         nodes = graph.get_nodes(lambda node: node.value >= 0)
#         assert nodes[:2] == graph.nodes[:2]

#     @pytest.mark.current
#     def test_graph_size(self, graph_with_nodes):
#         graph = graph_with_nodes
#         assert len(graph) == 2

#     @pytest.mark.current
#     def test_graph_get_edges(self, graph_unweighted):
#         graph = graph_unweighted
#         n1, n2 = graph.nodes[:2]
#         edges = graph.get_edges()
#         assert edges[0] == (n1, n2, 1)

#     @pytest.mark.current
#     def test_graph_get_edges(self, graph_weighted):
#         graph = graph_weighted
#         n1, n2 = graph.nodes[:2]
#         edges = graph.get_edges()
#         assert edges[0] == (n1, n2, 5)

#     @pytest.mark.current
#     def test_graph_get_connected_subgraph(self, graph_two_chains):
#         graph = graph_two_chains
#         subgraph = graph.get_subgraph_connected_from_head(graph.nodes[0])
#         assert len(subgraph) == len(graph) // 2

#     @pytest.mark.current
#     def test_graph_get_subgraph(self, graph_two_chains):
#         graph = graph_two_chains
#         s = len(graph)
#         subgraph = graph.get_subgraph_edgeless_copy(graph.nodes[s // 2 - 2 : s // 2 + 2])
#         n1, n2, n3, n4 = subgraph.nodes
#         assert len(subgraph) == 4
#         assert subgraph.get_edges() == [(n1, n2, 1), (n3, n4, 1)]


import numpy as np


class Test_Graphs:
    """tests for graph class"""

    def test_thing(self):
        g = BaseGraph()
        n0 = Node(0)
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        g.nodes = [n0, n1, n2, n3]
        g.adjs = np.array([[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 1, 1], [0, 1, 1, 0]])
        g.weights = np.array([[0, 2, 0, 0], [2, 0, 3, 4], [0, 3, 6, 7], [0, 4, 7, 0]])
        n4 = Node(1.5)
        adj_rule = lambda new, old: (new.value - old.value) ** 2 <= 1
        weight_rule = lambda new, old: (new.value + old.value) ** 2 // 4
        g.add_new_node(n4, adj_rule=adj_rule, weight_rule=weight_rule)
        print(g.nodes)
        print(g.adjs)
        print(g.weights)
        g2 = g.get_subgraph([1, 2, 3])
        print(g2.nodes)
        print(g2.adjs)
        print(g2.weights)
        g2.remove_node(n1)
        print(g.nodes)
        print(g.adjs)
        print(g.weights)
        print(g2.nodes)
        print(g2.adjs)
        print(g2.weights)

    @pytest.mark.current
    def test_2(self):
        g = Graph()
        n0 = Node(0)
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(3)
        print("g\n", g, "\n")
        g.add_new_node(n0, adj_rule=lambda x, y: [1, 2])
        print("g\n", g, "\n")
        g.add_new_node(n1, adj_rule=lambda x, y: [1, 3])
        print("g\n", g, "\n")
        g.add_new_node(n2, adj_rule=lambda x, y: [1, 4])
        print("g\n", g, "\n")
        g.add_edge(n2, n2, 12)
        print("g\n", g, "\n")
        g.remove_edge(n2, n1)
        print("g\n", g, "\n")
        print(g.get_adjs_indicies(n0))
        print(g.get_adjs_indicies(n1))
        print(g.get_adjs_indicies(n2))
