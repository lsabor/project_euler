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


class _BaseGraph(Set):
    """This is the most basic form of graph
    should be only used as parent class for specific forms of graphs

    nodes are saved in an array: [Node0, Node1, ...]
    edges (adjs) are saved in a n-by-n-by-depth matrix (n = number of nodes) where
    default depth is 2:
     adjs[:,:,0] is binary (0 or 1) matrix of directional edges initialized to 0
     adjs[:,:,1] is a float matrix of edge lengths initialized to 0

    Any further depth is user-defined to give edges additional properties,
    but default initialized to 0
    """

    name = "Base Graph"
    example = ""
    datatypes = [Node]
    directional = True
    weighted = True

    def __init__(self, *args, **kwargs):
        # initialize the nodes if given
        self.nodes = np.array(kwargs.pop("nodes", []))
        # then initialize the adjacency matrix
        adjs = kwargs.pop("adjs", self._initialized_matrix(depth=kwargs.get("depth", 2)))
        self.adjs = np.array(adjs)
        # if we have adjs but no nodes, populate nodes accordingly
        if not len(self.nodes) and len(self.adjs):
            self.nodes = np.array([Node() for _ in range(len(self.adjs))])
        if len(self.nodes) != len(self.adjs):
            raise ValueError(
                "Number of nodes given must match the first 2 dimensions of adjs given"
            )
        super().__init__(*args, **kwargs)

    def __repr__(self):
        """
        displays the list of Nodes, then the edge matrix, then the weights
        We transpose the dimensions of self.adjs so that the edges
        display separately from the weights
        e.g.
        self.nodes = [Node0, Node1]<-- Nodes
        self.adjs = [ [[0,   0],   <-- Node0 [edge, weight] with Node0
                       [1, 0.5]],  <-- Node0 [edge, weight] with Node1

                      [[1, 0.5],   <-- Node1 [edge, weight] with Node0
                       [0,   0]] ] <-- Node1 [edge, weight] with Node1
        displays as:
                    [Node0, Node1] <-- nodes
                    [ [[  0,   1], <-- edge matrix
                       [  1,   0]],

                      [[  0, 0.5], <-- weight matrix
                       [0.5,   0]] ]
        """
        return f"{self.nodes}\n{self.adjs.transpose(*range(2-len(self.adjs.shape),2))}"

    def __len__(self) -> int:
        return len(self.nodes)

    def _initialized_matrix(self, shape=None, default_value=0, depth=2, precision=np.float64):
        """returns an array initialized with default_value (0)
        to size len(self.nodes)^2-by-depth"""
        if shape is None:
            shape = (len(self.nodes), len(self.nodes))
            if depth > 1:
                shape += (depth,)
        return np.full(shape, default_value, dtype=precision)

    def _isInSet(self, node) -> bool:
        """return if node is found in graph"""
        return node in self.nodes

    def _expm(self, matrix):
        """
        returns a matrix with an additional row and column
        """
        shape = list(matrix.shape)
        shape[0] += 1
        shape[1] += 1
        new_matrix = np.zeros(shape, dtype=np.float64)
        new_matrix[:-1, :-1] = matrix
        return new_matrix

    def _addn(self, node):
        """direct node add"""
        self.nodes = np.append(self.nodes, node)

    def _updw(self, n1, n2, weight):
        """direct weight update"""
        self.adjs[n1, n2, 1] = weight

    def _upde(self, n1, n2, val):
        """direct edge update"""
        self.adjs[n1, n2] = val

    def _calc_adjs_directional(self, node, direction: bool, adjs=None, adj_rule=None) -> np.ndarray:
        if adjs is not None:
            return adjs
        if adj_rule is not None:
            if direction:
                return array([adj_rule(node, other) for other in self.nodes])
            return array([adj_rule(other, node) for other in self.nodes])
        shape = list(self.adjs.shape[1:])
        shape[0] += 1
        return np.zeros(shape)

    def _calc_adjs(self, node, to_adjs, from_adjs, adj_rule):
        to_adjs = self._calc_adjs_directional(node, direction=1, adjs=to_adjs, adj_rule=adj_rule)
        from_adjs = (
            to_adjs
            if not self.directional
            else self._calc_adjs_directional(node, direction=0, adjs=from_adjs, adj_rule=adj_rule)
        )
        return (to_adjs, from_adjs)

    def get_index(self, node_ref):
        """returns single index of node or index from node_ref"""
        if not isinstance(node_ref, Node):
            if node_ref < 0:
                node_ref += len(self)
            return node_ref
        return np.where(self.nodes == np.array(node_ref))[0][0]

    def get_node(self, node_ref):
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
            if max(node_refs) > len(self):
                raise ValueError(f"node ref too large {max(node_refs)}")
            return node_refs
        indicies = np.where([node in node_refs for node in self.nodes])[0]
        if len(indicies) < len(node_refs):
            raise ValueError("not all referenced nodes in graph")
        return indicies

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

    def get_adjs_array(self, node_ref) -> array:
        """returns the array of adjacencies with node_ref
        node_ref can be either a Node of an index of a node"""
        return self.adjs[self.get_index(node_ref)]

    def get_adjs_array_no_weight(self, node_ref) -> array:
        """returns the array of only adjacencies with node_ref
        node_ref can be either a Node of an index or a node"""
        adjs = self.get_adjs_array(node_ref)
        slices = (slice(len(adjs)),) + (0,) * (len(self.adjs.shape) - 2)
        return adjs[slices]

    def get_adjs_indicies(self, node_ref=None) -> array:
        """returns the indicies of adjacent nodes"""
        return np.where(self.get_adjs_array_no_weight(node_ref))[0]

    def add_new_node(self, node, to_adjs=None, from_adjs=None, adj_rule=None):
        """full-frills node adding
        adds node to self.nodes
        expands adjacency matrix
        populates adjacency matrix with adjs
        """
        self._addn(node)
        to_adjs, from_adjs = self._calc_adjs(node, to_adjs, from_adjs, adj_rule)

        self.adjs = self._expm(self.adjs)
        self.adjs[-1, :] = to_adjs
        self.adjs[:, -1] = from_adjs

    def remove_node(self, node_ref=None):
        """removes node from graph"""
        if node_ref is not None:
            self.remove_nodes([node_ref])

    def remove_nodes(self, node_refs=None):
        """removes nodes from graph"""
        if not node_refs:
            return
        node_refs = self.get_indicies(node_refs)
        self.nodes = np.delete(self.nodes, node_refs, axis=0)
        self.adjs = np.delete(self.adjs, node_refs, axis=0)
        self.adjs = np.delete(self.adjs, node_refs, axis=1)

    def add_edge(self, n0, n1, weight=1, edge=1):
        """adds an edge between 2 nodes"""
        n0, n1 = self.get_index(n0), self.get_index(n1)
        if isinstance(weight, Iterable):
            edge = [edge] + [_ for _ in weight]
        else:
            edge = [edge, weight]
        self._upde(n0, n1, edge)

    def remove_edge(self, n0, n1):
        """removes an edge between 2 nodes"""
        n0, n1 = self.get_index(n0), self.get_index(n1)
        self._upde(n0, n1, 0)

    def set_flags(self, nodes, flag):
        nodes = self.get_nodes_list(nodes)
        for node in nodes:
            node.flag = flag

    def clear_flags(self, nodes):
        self.set_flags(nodes, flag=None)

    def find_node(self, property):
        for node in self.nodes:
            if property(node):
                return node
        raise ValueError("No matching node")

    def get_subgraph(self, node_list):
        node_list = self.get_indicies_list(node_list)
        if node_list is None or len(node_list) == 0:
            return self.__class__()
        nodes = self.nodes[node_list]
        adjs = self.adjs[node_list, :][:, node_list]
        return self.__class__(nodes=nodes, adjs=adjs)

    def get_connected_subgraph(self, node):
        node = self.get_index(node)

        def get_connections(node, node_set):
            for i in self.get_adjs_indicies(node):
                if i not in node_set:
                    node_set = np.append(node_set, i)
                    node_set = get_connections(i, node_set)
            return node_set

        nodes = get_connections(node, np.array([node]))
        return self.get_subgraph(nodes)

    def lowest_cost_path(self, n0, n1):
        """uses dikjestra's algorithm to find the least costly path
        (in terms of edge weights) between n0 and n1
        """
        """
        start_node := start node
        end_node   := end node
        ei         := end node's index
        cn         := current node
        ci         := current node's index
        un         := unvisited node
        ui         := unvisited node index
        """
        # setup
        cn, end_node = self.get_node(n0), self.get_node(n1)
        start_node = cn
        # graph = self.get_connected_subgraph(cn)
        graph = self
        ci, ei = graph.get_index(n0), graph.get_index(n1)
        if not graph.isInSet(end_node):
            raise Exception("no path between n0 and n1")

        graph.set_flags(graph.nodes, "unseen")
        for node in graph.nodes:
            node.distance = float("inf")
        cn.distance = 0.0
        # visited = 0
        # this stores candidates for next search
        # TODO: change to min heap?
        next_up = dict()
        # search loop
        while ci != ei:
            # visited += 1
            # print("visited", visited, ci, end="\r")
            cn.flag = "visited"
            # get the unvisited nodes
            unvis_i = [i for i in self.get_adjs_indicies(ci) if graph.nodes[i] != "visited"]
            for ui in unvis_i:
                # for each unvisited node, we calculate its distance from c0
                un = graph.nodes[ui]
                distance = cn.distance + float(graph.adjs[ci, ui, 1])
                un.distance = min(un.distance, distance)

                # if the unvisited node isn't already known to be closer to c0
                # than our current distance, investigate it next
                if distance == un.distance:
                    un.path_parent = cn
                    # un.flag = "seen"
                    next_up[ui] = un
            nn, ni = None, None
            # grab our next node to search from based on distance
            for i, n in next_up.items():
                if nn is None or n.distance < nn.distance:
                    nn = n
                    ni = i
            del next_up[ni]
            cn, ci = nn, ni
        # print("total visited", visited, "of", len(self.nodes), end="\n")
        end_node = cn
        path = [end_node]
        while cn is not start_node:
            cn = cn.path_parent
            path.append(cn)
        path.reverse()
        return end_node.distance, path


class Graph(_BaseGraph):
    """This is weighted and directional"""

    name = "Graph"


class NonDirectionalGraph(_BaseGraph):

    name = "Non-Directional Graph"
    directional = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_edge(self, n0, n1, weight=1, edge=1):
        n0, n1 = self.get_index(n0), self.get_index(n1)

        super().add_edge(n0, n1, weight=weight, edge=edge)
        super().add_edge(n1, n0, weight=weight, edge=edge)

    def remove_edge(self, n0, n1):
        n0, n1 = self.get_index(n0), self.get_index(n1)
        self._upde(n0, n1, 0)
        self._upde(n1, n0, 0)


class NonWeightedGraph(_BaseGraph):

    name = "Non-Weighted Graph"
    weighted = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_edge(self, n0, n1, weight=1, edge=1):
        super().add_edge(n0, n1, weight=1, edge=edge)


class SimpleGraph(NonWeightedGraph, NonDirectionalGraph):
    """This graph is not weighted or directional"""

    name = "Simple Graph"
