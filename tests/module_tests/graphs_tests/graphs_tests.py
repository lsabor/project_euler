"""tests for graphs"""

import pytest

from maths.graphs.graphs2 import *


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


@pytest.fixture
def graph():
    return Graph()


@pytest.fixture
def populated_graph():
    n1 = Node(name="A")
    n2 = Node(name="B")
    return Graph(nodes=[n1, n2])


class Test_Graphs:
    """tests for the Graph object"""

    """
    BASIC functionality:
    X - make a graph 
    - add some nodes
    - add some edges
    - remove nodes
    - remove edges
    - search for node with specific value
    - search for edge with specific weight
    - edge can have or not have directions
    - edge can connect node to itself

    REFERENTIAL functionality like traversing:
    - get edges from a node
    - get nodes attached to an edge
    - get size of graph

    RELATIONAL functionality like search, subgraphing, etc.
    - return subgraph of connected nodes given some node as a graph
    - return arbitrary subgraph from nodes w/o outside connections as a graph object
    - find cliques of size
    - find shortest path between nodes
    - 

    """

    @pytest.mark.current
    def test_make_graph(self):
        Graph()

    @pytest.mark.current
    def test_graph_with_nodes(self):
        node = Node()
        graph = Graph(nodes=[node])
        assert graph.nodes == [node]

    @pytest.mark.current
    def test_graph_add_nodes(self, graph):
        n1 = Node()
        n2 = Node()
        graph.add_node(n1)
        graph.add_node(n2)
        assert graph.nodes == [n1, n2]

    @pytest.mark.current
    def test_graph_remove_node(self, populated_graph):
        graph = populated_graph
        n1, n2 = graph.nodes
        graph.remove_node(n1)
        assert graph.nodes == [n2]
        with pytest.raises(ValueError):
            graph.remove_node(n1)

    @pytest.mark.current
    def test_node_unweighted_adjs(self):
        n1 = Node(1)
        n2 = Node(2, adjs=[n1])

        assert n1.adjs == []
        assert n2.adjs == [n1]

        n1.add_adj(n2)
        assert n1.adjs == [n2]

    @pytest.mark.current
    def test_node_weighted_adjs(self):
        n1 = Node(1)
        n2 = Node(2, adjs=[(n1, 5)])

        assert n1.adjs == []
        assert n2.adjs == [(n1, 5)]

        n1.add_adj((n2, 7))
        assert n1.adjs == [(n2, 7)]

    @pytest.mark.current
    def test_node_remove_weighted_adj(self):
        n1 = Node(1)
        n2 = Node(2, adjs=[(n1, 5)])

        n2.remove_adj((n1, 5))
        assert n2.adjs == [(n1, 5)]

    @pytest.mark.current
    @pytest.mark.parametrize(
        "n1_ref,n2_ref",
        [
            (0, 1),
            ("A", "B"),  # TODO: add direct node refernce... maybe jsut another test :(
        ],
    )
    def test_graph_add_edge(self, populated_graph, n1_ref, n2_ref):
        graph = populated_graph
        graph.weighted = False
        n1, n2 = graph.nodes[:2]
        graph.add_edge(n1_ref, n2_ref)
        assert n1.adjs == [n2]
