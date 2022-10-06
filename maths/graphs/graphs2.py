"""This module holds basic graph functions"""

from maths.sets import Set


class Node:
    """an atom of a grpah
    value: value of the node
    adjs: list of adjacent nodes. Can be [node] or [(node,weight)]
    """

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

    def add_adj(self, adj):
        self.adjs.append(adj)

    def remove_adj(self, adj):
        """
        removes first adj that matches in self.adjs
        but if self.adjs are tuples (node,weight) and adj is just a node,
        this removes all adjacencies between self and adj
        """
        if type(adj) != type(self.adjs):
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

    def add_node(self, node=None, *args, **kwargs):
        if not node:
            node = Node(*args, **kwargs)
        self.nodes.append(node)

    def remove_node(self, node):
        self.nodes.remove(node)

    def get_node(self, node_ref):
        """returns referenced node from either index (int), name (str), or node (Node)"""
        match node_ref:
            case int():
                return self.nodes[node_ref]
            case str():
                return next(node for node in self.nodes if node.name == node_ref)
            case other:
                return node_ref

    def add_edge(self, n1_ref, n2_ref, weight=1):
        n1 = self.get_node(n1_ref)
        n2 = self.get_node(n2_ref)
        adj = (n2, weight) if self.weighted else n2
        n1.add_adj(n2)

    def remove_edge(self, n1_ref, n2_ref, weight=None):
        n1 = self.nodes(n1_ref) if isinstance(n1_ref, int) else n1_ref
        n2 = self.nodes(n2_ref) if isinstance(n2_ref, int) else n2_ref
        adj = (n2, weight) if weight else n2
        n1.remove_adj(n2)
