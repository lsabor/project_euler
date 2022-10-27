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

    def __init__(self, nodes=None, adjs=None, depth=1, *args, **kwargs):
        self.nodes = nodes if nodes else []
        self.adjs = adjs if adjs is not None else self.initialized_matrix(depth=depth)
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"{self.nodes}\n{self.adjs}"

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
        if isinstance(node_ref, int):
            return node_ref
        return self.nodes.index(node_ref)

    def get_node(self, node_ref=None):
        """returns a single node obj from node or index"""
        if isinstance(node_ref, Node):
            return node_ref
        return self.nodes[node_ref]

    def get_indicies(self, node_refs):
        """returns a list of indicies form node_refs
        node_refs should be list of nodes or indicies"""
        if not node_refs:
            return []
        first = node_refs[0]
        if isinstance(first, int):
            return node_refs
        return [self.nodes.index(node) for node in node_refs]

    def get_nodes(self, node_refs):
        """returns a list of nodes form node_refs
        node_refs should be list of nodes or indicies"""
        if not node_refs:
            return []
        first = node_refs[0]
        if isinstance(first, Node):
            return node_refs
        return [self.nodes[index] for index in node_refs]

    def get_indicies_list(self, node_refs=None):
        """returns a list of indicies representing node_refs
        deals well with singular node refs as an index or Node, as well as
        lists of those"""
        if node_refs is None:
            return [None]
        if isinstance(node_refs, Iterable):
            return self.get_indicies(list(node_refs))
        return [self.get_index(node_refs)]

    def get_nodes_list(self, node_refs=None):
        """returns a list of nodes representing node_refs
        deals well with singular node refs as an index or Node, as well as
        lists of those"""
        if node_refs is None:
            return [None]
        if isinstance(node_refs, Iterable):
            return self.get_nodes(list(node_refs))
        return [self.get_node(node_refs)]

    def _expm(self, new_array, matrix, dim):
        """returns the matrix a new column or row appended to it matching new_array
        if len(new_array) > len(matrix at dim), then new_array is truncated to that length
        """
        dim_size = matrix.shape[dim]
        if len(new_array) > dim_size:
            new_array = new_array[:dim_size]
        new_shape = list(matrix.shape)
        new_shape[dim] += 1
        print("hi", matrix.shape)
        matrix.resize(new_shape)
        print("bye", matrix.shape)
        matrix[-1, :, :] = new_array
        print(matrix)
        return matrix

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

    def get_adjs(self, node_ref=None) -> array:
        """returns the indicies of adjacent nodes"""
        return np.where(self.get_adjs_array(node_ref))[0]

    def remove_node(self, node_ref=None):
        if node_ref is not None:
            self.remove_nodes([node_ref])

    def remove_nodes(self, node_refs=None):
        """removes nodes from list of Nodes or indicies"""
        if not node_refs:
            return
        node_refs = self.get_indicies(node_refs)
        for node_ref in node_refs:
            del self.nodes[node_ref]
        self.adjs = np.delete(self.adjs, node_refs, axis=0)
        self.adjs = np.delete(self.adjs, node_refs, axis=1)
        self.weights = np.delete(self.weights, node_refs, axis=0)
        self.weights = np.delete(self.weights, node_refs, axis=1)

    def get_subgraph(self, node_list):
        node_list = self.get_indicies_list(node_list)
        if node_list[0] is None:
            return BaseGraph()
        nodes = [self.nodes[i] for i in node_list]
        adjs = self.adjs[node_list, :][:, node_list]
        weights = self.weights[node_list, :][:, node_list]
        return BaseGraph(nodes, adjs, weights)

    def copy(self):
        return BaseGraph(self.nodes, self.adjs, self.weights)

    def get_connected_subgraph(self, node):
        node = self.get_index(node)

        def get_connections(node, subgraph):
            adjs = self.get_adjs(node)
            for i in adjs:
                if i not in subgraph:
                    subgraph.add(i)
                    subgraph = subgraph.union(get_connections(i, subgraph))
            return subgraph

        return self.get_subgraph(get_connections(node, set([node])))

    def _addn(self, node):
        self.nodes.append(node)

    def _calc_to_adjs(self, node, adjs=None, adj_rule=None):
        if adjs is not None:
            return adjs
        return (
            np.zeros(len(self.nodes))
            if adj_rule is None
            else self.apply_rule_to_all(node, adj_rule)
        )

    def _calc_from_adjs(self, node, adjs=None, adj_rule=None):
        if adjs is not None:
            return adjs
        return (
            np.zeros(len(self.nodes))
            if adj_rule is None
            else self.apply_rule_from_all(node, adj_rule)
        )

    def _upde(self, n1, n2, val):
        self.adj[n1, n2] = val

    def add_flags(self, nodes, flag):
        nodes = self.get_nodes_list(nodes)
        for node in nodes:
            node.flag = flag

    def clear_flags(self, nodes):
        nodes = self.get_nodes_list(nodes)
        for node in nodes:
            node.flag = None


class DirectionalGraph(BaseGraph):

    name = "Directional Graph"
    directional = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_edge(self, n1, n2, val=1):
        n1, n2 = self.get_index(n1), self.get_index(n2)
        self._upde(n1, n2, val)

    def remove_edge(self, n1, n2, val=0):
        self.add_edge(n1, n2, val=val)

    def add_new_node(self, node, to_adjs=None, from_adjs=None, adj_rule=None):
        self._addn(node)

        to_adjs = self._calc_to_adjs(node, to_adjs, adj_rule)
        self.adjs = self._expm(to_adjs, self.adjs, dim=0)

        from_adjs = self._calc_from_adjs(node, from_adjs, adj_rule)
        self.adjs = self._expm(from_adjs, self.adjs, dim=1)


class NonDirectionalGraph(DirectionalGraph):

    name = "Non-Directional Graph"
    directional = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_edge(self, n1, n2, val=1):
        super().add_edge(n1, n2, val)
        super().add_edge(n2, n1, val)

    def _calc_from_adjs(self, node, adjs=None, adj_rule=None):
        """only call this after _calc_to_adjs"""
        # TODO: refactor?
        node_i = self.get_index(node)
        return np.concatenate(self.adjs[node_i], adj_rule(node, node))

    # def add_new_node(self, node, to_adjs=None, from_adjs=None, adj_rule=None):
    #     self._addn(node)

    #     to_adjs = self._calc_to_adjs(node, to_adjs, adj_rule)
    #     self.adjs = self._expm(to_adjs, self.adjs, dim=0)

    #     from_adjs = to_adjs
    #     self.adjs = self._expm(from_adjs, self.adjs, dim=1)


class DirectionalWeightedGraph(DirectionalGraph):

    name = "Directional Weighted Graph"
    weighted = True

    def __init__(self, weights=None, *args, **kwargs):
        super().__init__(weights, depth=2, *args, **kwargs)
        if weights is not None:
            self.adjs[:, :, 1] = weights

    def _updw(self, n1, n2, weight):
        self.adjs[n1, n2, 1] = weight

    def add_edge(self, n1, n2, edge=1, weight=1):
        n1, n2 = self.get_index(n1), self.get_index(n2)
        self._upde(n1, n2, array([edge, weight]))

    def remove_edge(self, n1, n2):
        self.add_edge(n1, n2, edge=0, weight=0)

    # def add_new_node(self, node, to_adjs=None, from_adjs=None, rule=None):
    #     self._addn(node)

    #     to_adjs = self._calc_to_adjs(node, to_adjs, rule)
    #     self.adjs = self._expm(to_adjs, self.adjs, dim=0)

    #     from_adjs = self._calc_from_adjs(node, from_adjs, rule)
    #     self.adjs = self._expm(from_adjs, self.adjs, dim=1)


class NonDirectionalWeightedGraph(NonDirectionalGraph):

    name = "Non-Directional Weighted Graph"
    weighted = True

    def __init__(self, weights=None, *args, **kwargs):
        super().__init__(weights, depth=2, *args, **kwargs)
        if weights is not None:
            self.adjs[:, :, 1] = weights

    def _updw(self, n1, n2, weight):
        self.adjs[n1, n2, 1] = weight
        self.adjs[n2, n1, 1] = weight

    def add_edge(self, n1, n2, edge=1, weight=1):
        n1, n2 = self.get_index(n1), self.get_index(n2)
        self._upde(n1, n2, array([edge, weight]))
        self._upde(n2, n1, array([edge, weight]))

    def remove_edge(self, n1, n2):
        self.add_edge(n1, n2, edge=0, weight=0)

    # def add_new_node(self, node, to_adjs=None, from_adjs=None, rule=None):
    #     self._addn(node)

    #     to_adjs = self._calc_to_adjs(node, to_adjs, rule)
    #     self.adjs = self._expm(to_adjs, self.adjs, dim=0)

    #     from_adjs = self._calc_from_adjs(node, from_adjs, rule)
    #     self.adjs = self._expm(from_adjs, self.adjs, dim=1)


class Graph(DirectionalWeightedGraph):
    """this is the most common graph"""

    name = "Graph"
