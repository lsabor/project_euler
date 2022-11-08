"""This module holds basic graph functions"""

from dataclasses import dataclass
from typing import Iterable
from maths.sets import Set
import itertools
import numpy as np
from numpy import array


@dataclass
class Node:
    value: int = 0


class BaseGraph(Set):
    """This is the most basic form of graph
    should be only used as parent class for specific forms of graphs
    """

    name = "Base Graph"
    example = ""
    datatypes = [Node]
    directional = True
    weighted = False

    def __init__(self, *args, **kwargs):
        self.nodes = kwargs.get("nodes", np.array([]))
        self.adjs = kwargs.get("adjs", self.initialized_matrix(depth=kwargs.get("depth", 1)))
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"{self.nodes}\n{self.adjs.transpose(*range(2-len(self.adjs.shape),2))}"

    def _isInSet(self, node) -> bool:
        """return if node is found in graph"""
        return node in self.nodes

    def initialized_matrix(self, default_value=0, depth=1):
        """returns an array initialized with default_value (0) to size len(self.nodes)^2"""
        shape = (len(self.nodes), len(self.nodes))
        if depth > 1:
            shape += (depth,)
        return np.full(shape, default_value)

    def get_index(self, node_ref=None):
        """returns single index of node or index from node_ref"""
        if not isinstance(node_ref, Node):
            return node_ref
        return np.where(self.nodes == np.array(node_ref))[0][0]

    def get_node(self, node_ref=None):
        """returns a single node obj from node or index"""
        if isinstance(node_ref, Node):
            return node_ref
        return self.nodes[node_ref]

    def get_indicies(self, node_refs):
        """returns a list of indicies form node_refs
        node_refs should be list of nodes or indicies"""
        if node_refs is None or len(node_refs) == 0:
            return []
        first = node_refs[0]
        if not isinstance(first, Node):
            return node_refs
        return np.where([node in node_refs for node in self.nodes])[0]

    def get_nodes(self, node_refs):
        """returns a list of nodes form node_refs
        node_refs should be list of nodes or indicies"""
        if node_refs is None or len(node_refs) == 0:
            return []
        first = node_refs[0]
        if isinstance(first, Node):
            return node_refs
        return self.nodes[node_refs]

    def get_indicies_list(self, node_refs=None):
        """returns a list of indicies representing node_refs
        deals well with singular node refs as an index or Node, as well as
        lists of those"""
        if node_refs is None:
            return []
        if isinstance(node_refs, Iterable):
            return self.get_indicies(node_refs)
        return [self.get_index(node_refs)]

    def get_nodes_list(self, node_refs=None):
        """returns a list of nodes representing node_refs
        deals well with singular node refs as an index or Node, as well as
        lists of those"""
        if node_refs is None:
            return [None]
        if isinstance(node_refs, Iterable):
            return self.get_nodes(node_refs)
        return [self.get_node(node_refs)]

    def _expm(self, matrix):
        """
        returns a matrix with an additional row and column
        """
        shape = list(matrix.shape)
        shape[0] += 1
        shape[1] += 1
        new_matrix = np.zeros(shape, dtype=int)
        new_matrix[:-1, :-1] = matrix
        return new_matrix

    def apply_rule_to_all(self, node, rule):
        """returns an array which is the rule applied to each node in self.nodes"""
        return array([rule(node, other) for other in self.nodes])

    def apply_rule_from_all(self, node, rule):
        """returns an array which is the rule applied to each node in self.nodes"""
        return array([rule(other, node) for other in self.nodes])

    def get_adjs_array(self, node_ref=None) -> array:
        """returns the array of adjacencies with node_ref
        node_ref can be either a Node of an index of a node"""
        return self.adjs[self.get_index(node_ref)]

    def get_adjs_only_array(self, node_ref=None) -> array:
        """returns the array of only adjacencies with node_ref
        node_ref can be either a Node of an index of a node"""
        adjs = self.get_adjs_array(node_ref)
        slices = (slice(len(adjs)),) + (0,) * (len(self.adjs.shape) - 2)
        return adjs[slices]

    def get_adjs_indicies(self, node_ref=None) -> array:
        """returns the indicies of adjacent nodes"""
        return np.where(self.get_adjs_only_array(node_ref))[0]

    def remove_node(self, node_ref=None):
        if node_ref is not None:
            self.remove_nodes([node_ref])

    def remove_nodes(self, node_refs=None):
        """removes nodes from list of Nodes or indicies"""
        if not node_refs:
            return
        node_refs = self.get_indicies(node_refs)
        self.nodes = np.delete(self.nodes, node_refs, axis=0)
        self.adjs = np.delete(self.adjs, node_refs, axis=0)
        self.adjs = np.delete(self.adjs, node_refs, axis=1)

    def get_subgraph(self, node_list):
        node_list = self.get_indicies_list(node_list)
        if node_list is None or len(node_list) == 0:
            return self.__class__()
        nodes = self.nodes[node_list]
        adjs = self.adjs[node_list, :][:, node_list]
        return self.__class__(nodes=nodes, adjs=adjs)

    def copy(self):
        return self.__class__(nodes=self.nodes, ajds=self.adjs)

    def get_connected_subgraph(self, node):
        node = self.get_index(node)

        def get_connections(node, node_set):
            breakpoint()
            for i in self.get_adjs_indicies(node):
                if i not in node_set:
                    node_set = np.append(node_set, i)
                    node_set = get_connections(i, node_set)
            return node_set

        nodes = get_connections(node, np.array([node]))
        return self.get_subgraph(nodes)

    def _addn(self, node):
        self.nodes = np.append(self.nodes, node)

    def _calc_to_adjs(self, node, adjs=None, adj_rule=None):
        if adjs is not None:
            return adjs
        return (
            np.zeros((self.adjs[0].shape[0] + 1,) + tuple(self.adjs[0].shape[1:]))
            if adj_rule is None
            else self.apply_rule_to_all(node, adj_rule)
        )

    def _calc_from_adjs(self, node, adjs=None, adj_rule=None):
        if adjs is not None:
            return adjs
        return (
            np.zeros((self.adjs[0].shape[0] + 1,) + tuple(self.adjs[0].shape[1:]))
            if adj_rule is None
            else self.apply_rule_from_all(node, adj_rule)
        )

    def _upde(self, n1, n2, val):
        self.adjs[n1, n2] = val

    def add_new_node(self, node, to_adjs=None, from_adjs=None, adj_rule=None):
        self._addn(node)

        to_adjs = self._calc_to_adjs(node, to_adjs, adj_rule)
        from_adjs = self._calc_from_adjs(node, from_adjs, adj_rule)

        self.adjs = self._expm(self.adjs)
        self.adjs[-1, :] = to_adjs
        self.adjs[:, -1] = from_adjs

    def set_flags(self, nodes, flag):
        nodes = self.get_nodes_list(nodes)
        for node in nodes:
            node.flag = flag

    def clear_flags(self, nodes):
        self.set_flags(nodes, flag=None)


class DirectionalGraph(BaseGraph):

    name = "Directional Graph"
    directional = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_edge(self, n1, n2, edge=1):
        n1, n2 = self.get_index(n1), self.get_index(n2)
        self._upde(n1, n2, edge)

    def remove_edge(self, n1, n2, edge=0):
        self.add_edge(n1, n2, edge)


class NonDirectionalGraph(DirectionalGraph):

    name = "Non-Directional Graph"
    directional = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_edge(self, n1, n2, edge=1):
        super().add_edge(n1, n2, edge)
        super().add_edge(n2, n1, edge)

    def _calc_from_adjs(self, node, adjs=None, adj_rule=None):
        """only call this after _calc_to_adjs"""
        node_i = self.get_index(node)
        return np.concatenate(self.adjs[node_i], adj_rule(node, node))


class DirectionalWeightedGraph(DirectionalGraph):

    name = "Directional Weighted Graph"
    weighted = True

    def __init__(self, weights=None, *args, **kwargs):
        super().__init__(weights, depth=2, *args, **kwargs)
        if weights is not None:
            self.adjs[:, :, 1] = weights

    def _updw(self, n1, n2, weight):
        self.adjs[n1, n2, 1] = weight

    def add_edge(self, n1, n2, weight=1, edge=1):
        super().add_edge(n1, n2, edge=[edge, weight])

    def lowest_cost_path(self, n1, n2):
        cn, end_node = self.get_node(n1), self.get_node(n2)
        n0 = cn
        # graph = self.get_connected_subgraph(cn)
        graph = self
        ci, ei = graph.get_index(n1), graph.get_index(n2)
        if not graph.isInSet(end_node):
            raise Exception("no path between n1 and n2")

        graph.set_flags(graph.nodes, "unseen")
        for node in graph.nodes:
            node.distance = float("inf")
        cn.flag = "visited"
        cn.distance = 0.0
        visited = 0
        while ci != ei:
            visited += 1
            print("visited", visited, ci, end="\r")
            cn.flag = "visited"
            adjs = graph.adjs[ci]
            adjs_i = np.where(adjs[:, 0])[0]
            unvis_i = []
            for i in adjs_i:
                if graph.nodes[i].flag != "visited":
                    unvis_i.append(i)
            adjs_i = unvis_i
            adjs_n = graph.nodes[adjs_i]
            for ai, an in zip(adjs_i, adjs_n):
                distance = cn.distance + float(adjs[ai, 1])
                an.distance = (
                    distance if an.distance == float("inf") else min(an.distance, distance)
                )
                if distance == an.distance:
                    an.path_parent = cn
                    an.flag = "seen"
            nn, ni = None, None
            for i, n in enumerate(graph.nodes):
                if n.flag == "seen":
                    if nn is None or n.distance < nn.distance:
                        nn = n
                        ni = i
            cn, ci = nn, ni
        print("total visited", visited, "of", len(self.nodes), end="\n")

        end_node = cn
        path = [end_node]
        while cn is not n0:
            cn = cn.path_parent
            path.append(cn)
        path.reverse()

        return end_node.distance, path


class NonDirectionalWeightedGraph(DirectionalWeightedGraph):

    name = "Non-Directional Weighted Graph"
    weighted = True

    def __init__(self, weights=None, *args, **kwargs):
        super().__init__(weights, *args, **kwargs)

    def _updw(self, n1, n2, weight):
        super()._updw(n1, n2, weight)
        super()._updw(n2, n1, weight)

    def add_edge(self, n1, n2, weight=1, edge=1):
        super().add_edge(n1, n2, weight, edge)
        super().add_edge(n2, n1, weight, edge)


class Graph(DirectionalWeightedGraph):
    """this is the most common graph"""

    name = "Graph"
