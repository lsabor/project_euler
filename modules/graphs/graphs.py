"""This module holds basic graph functions"""


class Node:
    """the basic atom of a graph"""

    def __init__(self, value=None, flag=None):
        self.value = value
        self.flag = flag
        self.outbound = set()
        self.in_bound = set()

    def __repr__(self):
        return str(self.value)

    def getAdjacentEdges(self) -> set["Edge"]:
        return self.outbound.union(self.in_bound)


class Edge:
    """connects two nodes, can be directional"""

    def __init__(self, node0: Node, node1: Node, length=None, direction=0, flag=None):
        self.node0 = node0
        self.node1 = node1
        self.length = length
        self.nodes = set((self.node0, self.node1))
        self.flag = flag
        self.updateDirection(direction)

    def __repr__(self):
        match self._direction:
            case 1:
                init_tag = "-"
                last_tag = ">"
            case 0:
                init_tag = "<"
                last_tag = ">"
            case -1:
                init_tag = "<"
                last_tag = "-"
        return f'{self.node0} {init_tag}{self.length if self.length else ""}{last_tag} {self.node1}'

    def getDestinies(self) -> set[Node]:
        """returns the nodes which are in the direction of the edge"""
        return set([node for node in self.nodes if self in node.in_bound])

    def getGenesises(self) -> set[Node]:
        """returns the nodes which are from the direction of the edge"""
        return set([node for node in self.nodes if self in node.outbound])

    def hasNode(self, node: Node) -> bool:
        return node in self.nodes

    def doesDirectionallyConnectNodes(self, startnode: Node, endnode: Node) -> bool:
        """returns if self connects startnode to endnode directionally"""
        return startnode in self.getGenesises() and endnode in self.getDestinies()

    def createMateWithNodes(self, startnode: Node, endnode: Node):
        """add a directional connection between startnode and endnode"""
        startnode.outbound.add(self)
        endnode.in_bound.add(self)

    def removeMateWithNodes(self, startnode: Node, endnode: Node):
        """removes a directional edge"""
        try:
            startnode.outbound.remove(self)
            endnode.in_bound.remove(self)
        except:
            pass

    def updateDirection(self, direction: int):
        """makes sure that the appropriate direction is established between
        attached nodes"""
        self._direction = direction
        match self._direction:
            case 1:
                self.createMateWithNodes(self.node0, self.node1)
                self.removeMateWithNodes(self.node1, self.node0)
            case 0:
                self.createMateWithNodes(self.node0, self.node1)
                self.createMateWithNodes(self.node1, self.node0)
            case -1:
                self.createMateWithNodes(self.node1, self.node0)
                self.removeMateWithNodes(self.node0, self.node1)


# TODO: keep cleaning from here
class Graph:
    def __init__(self, edges=None, nodes=None, head=None):

        self.nodes = set()
        self.edges = set()
        if nodes:
            self.nodes = nodes
            self.edges = self.getEdgesFromNodes(nodes)
        if edges:
            for edge in edges:
                self.nodes.add(edge.node0)
                self.nodes.add(edge.node1)
                self.edges.add(edge)
                self.edges = self.edges.union(self.getEdgesFromNodes(self.nodes))
        self.sethead(head)

    def __repr__(self):
        output = "EDGES:\n"
        for edge in self.edges:
            output += f"{edge}\n"
        output += "NODES:\n" + str(self.nodes)
        return output

    def __len__(self):
        return len(self.nodes)

    def remove(self, node):
        for edge in node.getAdjacentEdges():
            if edge in self.edges:
                self.edges.remove(edge)
        self.nodes.remove(node)

    def getEdgesFromNodes(self, nodes):
        if not nodes:
            return set()
        edges = set()
        for node in nodes:
            new_edges = set(
                edge
                for edge in node.getAdjacentEdges()
                if ((edge.node0 in nodes) and (edge.node1 in nodes))
            )
            edges = edges.union(new_edges)
        return edges

    def getNodesFromEdges(self, edges):
        if not edges:
            return set()
        nodes = set()
        for edge in edges:
            new_nodes = set(edge.nodes)
            nodes = nodes.union(new_nodes)
        return nodes

    def addNodeSet(self, nodes):
        self.nodes = self.nodes.union(nodes)
        new_edges = self.getEdgesFromNodes(nodes)
        self.edges = self.edges.union(new_edges)

    def addNode(self, node):
        self.addNodeSet(set([node]))

    def addEdgeSet(self, edges):
        self.edges = self.edges.union(edges)
        new_nodes = self.getNodesFromEdges(edges)
        self.nodes = self.nodes.union(new_nodes)

    def addEdge(self, edge):
        self.addEdgeSet(set([edge]))

    def sethead(self, new_head: Node):
        if new_head and new_head not in self.nodes:
            self.addNode(new_head)
        self._head = new_head

    def getHead(self):
        return self._head

    def hasNode(self, node: Node) -> bool:
        return node in self.nodes

    def hasNodes(self, nodes) -> bool:
        return all([self.hasNode(node) for node in nodes])

    def getAdjacentNodes(self, node: Node):
        edges = node.getAdjacentEdges()
        adjacent_nodes = set()
        for edge in edges:
            adjacent_nodes = adjacent_nodes.union(edge.nodes)
        adjacent_nodes.remove(node)
        return adjacent_nodes

    def getOutboundAdjacentNodes(self, node: Node):
        edges = node.getAdjacentEdges()
        outbound_adjacent_nodes = set()
        for edge in edges:
            outbound_adjacent_nodes = outbound_adjacent_nodes.union(edge.getDestinies())
        if node in outbound_adjacent_nodes:
            outbound_adjacent_nodes.remove(node)
        return outbound_adjacent_nodes

    def getInBoundAdjacentNodes(self, node: Node):
        edges = node.getAdjacentEdges()
        in_bound_adjacent_nodes = set()
        for edge in edges:
            in_bound_adjacent_nodes = in_bound_adjacent_nodes.union(
                edge.get_genisises()
            )
        if node in in_bound_adjacent_nodes:
            in_bound_adjacent_nodes.remove(node)
        return in_bound_adjacent_nodes

    def markNodes(self, nodes, flag_name: str):
        for node in nodes:
            node.flag = flag_name

    def markNode(self, node: Node, flag_name: str):
        self.markNodes(set([node]), flag_name)

    def resetNodes(self, nodes):
        self.markNodes(nodes, flag_name=None)

    def resetNode(self, node: Node):
        self.markNode(node, flag=None)

    # def get_adj_nodes_with_criteria(self,node, criteria:function):
    #     pass

    def getAdjacentNodesWithFlag(self, node: Node, flag_name: str):
        return set(
            [node for node in self.getAdjacentNodes(node) if node.flag == flag_name]
        )

    def getAdjacentNodesWithoutFlag(self, node: Node, flag_name: str):
        return set(
            [node for node in self.getAdjacentNodes(node) if node.flag != flag_name]
        )

    def getOutboundAdjacentNodesWithFlag(self, node: Node, flag_name: str):
        return set(
            [
                node
                for node in self.getOutboundAdjacentNodes(node)
                if node.flag == flag_name
            ]
        )

    def getOutboundAdjacentNodesWithoutFlag(self, node: Node, flag_name: str):
        return set(
            [
                node
                for node in self.getOutboundAdjacentNodes(node)
                if node.flag != flag_name
            ]
        )

    def getInBoundAdjacentNodesWithFlag(self, node: Node, flag_name: str):
        return set(
            [
                node
                for node in self.getInBoundAdjacentNodes(node)
                if node.flag == flag_name
            ]
        )

    def getInBoundAdjacentNodesWithoutFlag(self, node: Node, flag_name: str):
        return set(
            [
                node
                for node in self.getInBoundAdjacentNodes(node)
                if node.flag != flag_name
            ]
        )

    def getAllConnectedNodes(self, node):
        self.resetNodes(self.nodes)

        def exploreDeep(node, node_set):
            to_explore = self.getAdjacentNodesWithoutFlag(node, "EXPLORED")
            self.markNodes(to_explore, "EXPLORED")
            node_set.add(node)
            for new_node in to_explore:
                node_set = node_set.union(exploreDeep(new_node, node_set))
            return node_set

        all_connected_nodes = exploreDeep(node, set([node]))
        return all_connected_nodes

    def connectionExists(self, node0, node1):
        return node0 in self.getAllConnectedNodes(node1)

    def getAllDirectionallyConnectedNodes(self, node):
        self.resetNodes(self.nodes)

        def exploreDeep(node, node_set):
            to_explore = self.getOutboundAdjacentNodesWithoutFlag(node, "EXPLORED")
            self.markNodes(to_explore, "EXPLORED")
            node_set.add(node)
            for new_node in to_explore:
                node_set = node_set.union(exploreDeep(new_node, node_set))
            return node_set

        all_connected_nodes = exploreDeep(node, set([node]))
        return all_connected_nodes

    def getAllDirectionallyConnectedEdges(self, node):
        edges = set()
        for n in self.getAllDirectionallyConnectedNodes(node):
            edges = edges.union(n.outbound)
        return edges

    def directionalConnectionExists(self, startnode, endnode):
        return endnode in self.getAllDirectionallyConnectedNodes(startnode)

    def shortestPathDirectional(self, n0, n1):
        # returns distance, and path
        connected_nodes = self.getAllDirectionallyConnectedNodes(n0)
        if n1 not in connected_nodes:
            raise Exception("NO PATH EXISTS")
        for node in connected_nodes:
            node.flag = "UNSEEN"
            node.distance = "inf"
        n0.distance = 0

        current_node = n0

        while current_node is not n1:
            current_node.flag = "VISITED"
            adjacent_nodes = self.getOutboundAdjacentNodes(current_node)
            for n in adjacent_nodes:
                relevant_edges = [
                    edge
                    for edge in self.edges
                    if edge.doesDirectionallyConnectNodes(current_node, n)
                ]
                new_distance = current_node.distance + min(
                    [edge.length for edge in relevant_edges]
                )
                n.distance = (
                    new_distance
                    if n.distance == "inf"
                    else min(n.distance, new_distance)
                )
                if new_distance == n.distance:
                    n.path_parent = current_node
                    n.flag = "SEEN"
            next_node = None
            for node in connected_nodes:
                if node.flag == "SEEN":
                    next_node = (
                        node
                        if next_node is None
                        else (
                            next_node if next_node.distance <= node.distance else node
                        )
                    )
            current_node = next_node

        end_node = current_node
        path = [end_node]
        while current_node is not n0:
            current_node = current_node.path_parent
            path.append(current_node)
        path.reverse()

        return end_node.distance, path

    def getSubgraph(self, nodes=None, edges=None):
        if not (nodes or edges):
            return Graph()
        if nodes:
            return Graph(nodes=nodes)
        if edges:
            nodes = set()
            for edge in edges:
                nodes.add(edge.node0)
                nodes.add(edge.node1)
            return Graph(nodes=nodes)

    def findCliques(self, size: int):
        """returns the cliques (subgraph will all interconnected nodes)
        of given size"""
        cliques = []
        if len(self) < size:
            return cliques
        if size == 2:
            # find all pairs in graph
            for edge in self.edges:
                cliques.append(set([edge.node0, edge.node1]))
        else:
            untested = set(self.nodes)
            for node in self.nodes:
                nodes = set()
                for edge in node.getAdjacentEdges():
                    nodes = nodes.union(
                        set(node for node in edge.nodes if node in untested)
                    )
                untested.remove(node)
                if nodes:
                    nodes.remove(node)
                edges = set()
                for n in nodes:
                    for edge in n.getAdjacentEdges():
                        if (edge.node0 in nodes) and (edge.node1 in nodes):
                            edges.add(edge)
                local_graph = Graph(nodes=nodes, edges=edges)
                new_cliques = local_graph.findCliques(size=size - 1)
                for clique in new_cliques:
                    clique.add(node)
                    cliques.append(clique)
        return cliques


def nodify(array) -> list:
    node_array = [[Node(val) for val in row] for row in array]
    return node_array
