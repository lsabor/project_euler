"""tests for graphs"""

import string
import pytest

from maths.graphs.graphs import *


@pytest.fixture
def graph():
    return Graph()


@pytest.fixture
def populated_graph_basic():
    n1 = Node(0)
    n2 = Node(1)
    return Graph(nodes=[n1, n2], adjs=np.array([[[0, 0], [1, 0.5]], [[1, 0.5], [0, 0]]]))


@pytest.fixture
def graph_two_chains(graph):
    for index, letter in enumerate(string.ascii_uppercase):
        node = Node(value=index)
        node.name = letter
        graph.add_new_node(node)
    count = len(graph.nodes)
    for i in range(count - 1):
        graph.add_edge(i, i + 1)
        graph.add_edge(i + 1, i)
    graph.remove_edge(count // 2 - 1, count // 2)
    graph.remove_edge(count // 2, count // 2 - 1)

    return graph


class Test_Graphs:
    """tests for the Graph object"""

    """
    BASIC functionality:
    - make an empty graph
    - make a graph nodes only (populates adjs)
    - make a graph adjs only (populates Nodes)
    - make a graph nodes and adjs populated
    - given empty graph:
        - add some nodes
        - add some edges
    - given populated graph
        - remove nodes
        - remove edges
        - search for nodes that match condition
        - get size of graph with len

    RELATIONAL functionality like search, subgraphing, etc.
    - return subgraph of connected nodes given some node as a graph
    - return arbitrary subgraph from nodes w/o outside connections as a graph object
    - find shortest path between nodes
    - find clique(s?) of size

    """

    @pytest.mark.current
    def test_make_graph(self):
        Graph()

    @pytest.mark.current
    def test_graph_with_nodes_only(self):
        node = Node()
        graph = Graph(nodes=[node])
        assert graph.nodes == [node]
        assert len(graph.adjs) == 1

    @pytest.mark.current
    def test_graph_with_edges_only(self):
        adjs = [[[0, 0], [1, 0.5]], [[1, 0.5], [0, 0]]]
        graph = Graph(adjs=adjs)
        assert len(graph.nodes) == 2

    @pytest.mark.current
    def test_graph_with_nodes_and_edges(self):
        n0 = Node(0)
        n1 = Node(1)
        adjs = [[[0, 0], [1, 0.5]], [[1, 0.5], [0, 0]]]
        graph = Graph(nodes=[n0, n1], adjs=adjs)
        assert len(graph.nodes) == 2
        assert len(graph.adjs) == 2

    @pytest.mark.current
    def test_add_nodes(self, graph):
        n0 = Node(0)
        n1 = Node(1)
        graph.add_new_node(n0)
        graph.add_new_node(n1)
        assert len(graph.nodes) == 2

    @pytest.mark.current
    def test_add_edge(self, populated_graph_basic):
        graph = populated_graph_basic
        graph.add_edge(0, 1, weight=1.5)
        assert graph.adjs[0, 1, 1] == 1.5

    @pytest.mark.current
    def test_remove_node(self, populated_graph_basic):
        graph = populated_graph_basic
        n0, n1 = graph.nodes
        graph.remove_node(n0)
        assert graph.nodes[0] is n1
        with pytest.raises(ValueError):
            graph.remove_node(n0)

    @pytest.mark.current
    def test_remove_edge(self, populated_graph_basic):
        graph = populated_graph_basic
        assert graph.adjs[0, 1, 1] != 0
        graph.remove_edge(0, 1)
        assert graph.adjs[0, 1, 1] == 0

    @pytest.mark.current
    def test_get_specific_node(self, populated_graph_basic):
        graph = populated_graph_basic
        node = graph.find_node((lambda node: node.value == 1))
        assert node.value == 1

    @pytest.mark.current
    def test_len(self, populated_graph_basic):
        graph = populated_graph_basic
        assert len(graph) == 2

    @pytest.mark.current
    def test_get_subgraph(self, graph_two_chains):
        graph = graph_two_chains
        subgraph = graph.get_subgraph(range(0, len(graph), 2))
        assert len(subgraph) == len(graph) // 2

    @pytest.mark.current
    def test_get_connected_subgraph(self, graph_two_chains):
        graph = graph_two_chains
        subgraph = graph.get_connected_subgraph(graph.nodes[0])
        assert len(subgraph) == len(graph) // 2

    @pytest.mark.current
    def test_get_shortest_path(self, graph_two_chains):
        graph = graph_two_chains
        cost, path = graph.lowest_cost_path(*graph.nodes[[0, 12]])
        assert cost == 12
