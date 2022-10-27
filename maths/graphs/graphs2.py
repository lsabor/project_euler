"""This module holds basic graph functions"""

from copy import copy
from maths.sets import Set
import itertools


class Node:
    """an atom of a grpah
    value: value of the node
    adjs: list of adjacent nodes. Can be [node] or [(node,weight)]
    """

    flag = None

    def __init__(
        self,
        value=None,
        adjs=None,
        name=None,
    ) -> None:
        self.value = value
        self.adjs = adjs if adjs else []
        self.name = name

    def __repr__(self):
        return str(self.name) if self.name else str(self.value)

    def add_adj(self, node=None, weight=1, adj=None):
        if adj:
            self.adjs.append(adj)
        else:
            self.adjs.append((node, weight))

    def remove_adj(self, adj):
        """
        removes first adj that matches in self.adjs
        but if self.adjs are tuples (node,weight) and adj is just a node,
        this removes all adjacencies between self and adj
        """
        if isinstance(adj, Node):
            self.adjs = [x for x in self.adjs if x[0] is not adj]
        else:
            self.adjs.remove(adj)


class Graph(Set):

    name = "Graph"
    exmple = "Edges: [A -> B, A -> C, C -> B, ...]"
    datatypes = [Node]

    def __init__(self, nodes=None, weighted=False, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.nodes = nodes if nodes else []
        self.weighted = weighted

    def __len__(self):
        return len(self.nodes)

    def add_node(self, node=None, *args, **kwargs):
        if not node:
            node = Node(*args, **kwargs)
        self.nodes.append(node)

    def remove_node(self, node):
        self.nodes.remove(node)

    def get_node_from_ref(self, node_ref):
        """returns referenced node from either index (int), name (str), or node (Node)"""
        match node_ref:
            case int():
                return self.nodes[node_ref]
            case str():
                return next(node for node in self.nodes if node.name == node_ref)
            case other:
                return node_ref

    def add_edge(self, n1_ref, n2_ref, weight=1):
        n1 = self.get_node_from_ref(n1_ref)
        n2 = self.get_node_from_ref(n2_ref)
        n1.add_adj(n2, weight)

    def remove_edge(self, n1_ref, n2_ref, weight=None):
        # n1 = self.nodes[n1_ref] if isinstance(n1_ref, int) else n1_ref
        # n2 = self.nodes[n2_ref] if isinstance(n2_ref, int) else n2_ref
        n1 = self.get_node_from_ref(n1_ref)
        n2 = self.get_node_from_ref(n2_ref)
        adj = (n2, weight) if weight else n2
        n1.remove_adj(adj)

    def get_node(self, condition):
        for node in self.nodes:
            if condition(node):
                return node
        raise ValueError("no nodes match condition")

    def get_node_by_name(self, name):
        return self.get_node(lambda node: node.name == name)

    def get_node_by_value(self, value):
        return self.get_node(lambda node: node.value == value)

    def get_nodes(self, condition):
        return [node for node in self.nodes if condition(node)]

    def get_edges(self):
        adjs = []
        for node in self.nodes:
            for adj in node.adjs:
                adjs.append((node,) + adj)
        return adjs

    def add_flags(self, nodes, flag):
        nodes = nodes if nodes else self.nodes
        for node in nodes:
            node.flag = flag

    def clear_flags(self, nodes=None):
        self.add_flags(nodes, None)

    def get_subgraph_connected_from_head(self, node):
        nodes = [node]
        node.flag = "explored"

        def explore_node(node):
            for adj in node.adjs:
                new_node = adj[0]
                if new_node.flag == "explored":
                    continue
                new_node.flag = "explored"
                nodes.append(new_node)
                explore_node(new_node)

        explore_node(node)
        graph = Graph(nodes=nodes)
        graph.clear_flags()
        return graph

    def get_subgraph_edgecopy(self, nodes):
        """expensive
        copies each node in nodes, then copies only the relevant edges
        over to the new graph... probably want to rethink this.
        """
        graph = Graph(weighted=self.weighted)
        new_nodes = [copy(node) for node in nodes]
        for new_node in new_nodes:
            for j, adj in enumerate(new_node.adjs):
                found = False
                adj_node = adj[0]
                for o, node in enumerate(nodes):
                    if adj_node == node:
                        new_node.adjs[j] = (new_nodes[o], new_node.adjs[j][1])
                        found = True
                        break
                if not found:
                    new_node.adjs[j] = None
            new_node.adjs = [adj for adj in new_node.adjs if adj is not None]
            graph.add_node(new_node)
        return graph
