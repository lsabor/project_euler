# This module holds basic graph functions


class Node:
    def __init__(self, value=None, flag=None):
        self.value = value
        self.flag = flag
        self.outbound = set()
        self.in_bound = set()

    def __repr__(self):
        return str(self.value)

    def get_adjacent_edges(self):
        return self.outbound.union(self.in_bound)


class Edge:
    def __init__(self, node0: Node, node1: Node, length=None, direction=0, flag=None):
        self.node0 = node0
        self.node1 = node1
        self.length = length
        self.nodes = set((self.node0, self.node1))
        self.flag = flag
        self.update_direction(direction)

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

    def get_destinies(self):
        return set([node for node in self.nodes if self in node.in_bound])

    def get_genesises(self):
        return set([node for node in self.nodes if self in node.outbound])

    def has_node(self, node):
        return node in self.nodes

    def does_directionally_connect_nodes(self, startnode: Node, endnode: Node):
        return startnode in self.get_genesises() and endnode in self.get_destinies()

    def create_mate_with_nodes(self, startnode, endnode):
        startnode.outbound.add(self)
        endnode.in_bound.add(self)

    def remove_mate_with_nodes(self, startnode, endnode):
        try:
            startnode.outbound.remove(self)
            endnode.in_bound.remove(self)
        except:
            pass

    def update_direction(self, direction):
        self._direction = direction
        match self._direction:
            case 1:
                self.create_mate_with_nodes(self.node0, self.node1)
                self.remove_mate_with_nodes(self.node1, self.node0)
            case 0:
                self.create_mate_with_nodes(self.node0, self.node1)
                self.create_mate_with_nodes(self.node1, self.node0)
            case -1:
                self.create_mate_with_nodes(self.node1, self.node0)
                self.remove_mate_with_nodes(self.node0, self.node1)


class Graph:
    def __init__(self, edges=None, nodes=None, head=None):

        self.nodes = set()
        self.edges = set()
        if nodes:
            self.nodes = nodes
            self.edges = self.get_edges_from_nodes(nodes)
        if edges:
            for edge in edges:
                self.nodes.add(edge.node0)
                self.nodes.add(edge.node1)
                self.edges.add(edge)
                self.edges = self.edges.union(self.get_edges_from_nodes(self.nodes))
        self.set_head(head)

    def __repr__(self):
        output = "EDGES:\n"
        for edge in self.edges:
            output += f"{edge}\n"
        output += "NODES:\n" + str(self.nodes)
        return output

    def __len__(self):
        return len(self.nodes)

    def remove(self, node):
        for edge in node.get_adjacent_edges():
            if edge in self.edges:
                self.edges.remove(edge)
        self.nodes.remove(node)

    def get_edges_from_nodes(self, nodes):
        if not nodes:
            return set()
        edges = set()
        for node in nodes:
            new_edges = set(
                edge
                for edge in node.get_adjacent_edges()
                if ((edge.node0 in nodes) and (edge.node1 in nodes))
            )
            edges = edges.union(new_edges)
        return edges

    def get_nodes_from_edges(self, edges):
        if not edges:
            return set()
        nodes = set()
        for edge in edges:
            new_nodes = set(edge.nodes)
            nodes = nodes.union(new_nodes)
        return nodes

    def add_node_set(self, nodes):
        self.nodes = self.nodes.union(nodes)
        new_edges = self.get_edges_from_nodes(nodes)
        self.edges = self.edges.union(new_edges)

    def add_node(self, node):
        self.add_node_set(set([node]))

    def add_edge_set(self, edges):
        self.edges = self.edges.union(edges)
        new_nodes = self.get_nodes_from_edges(edges)
        self.nodes = self.nodes.union(new_nodes)

    def add_edge(self, edge):
        self.add_edge_set(set([edge]))

    def set_head(self, new_head: Node):
        if new_head and new_head not in self.nodes:
            self.add_node(new_head)
        self._head = new_head

    def get_head(self):
        return self._head

    def has_node(self, node: Node) -> bool:
        return node in self.nodes

    def has_nodes(self, nodes) -> bool:
        return all([self.has_node(node) for node in nodes])

    def get_adjacent_nodes(self, node: Node):
        edges = node.get_adjacent_edges()
        adjacent_nodes = set()
        for edge in edges:
            adjacent_nodes = adjacent_nodes.union(edge.nodes)
        adjacent_nodes.remove(node)
        return adjacent_nodes

    def get_outbound_adjacent_nodes(self, node: Node):
        edges = node.get_adjacent_edges()
        outbound_adjacent_nodes = set()
        for edge in edges:
            outbound_adjacent_nodes = outbound_adjacent_nodes.union(
                edge.get_destinies()
            )
        if node in outbound_adjacent_nodes:
            outbound_adjacent_nodes.remove(node)
        return outbound_adjacent_nodes

    def get_in_bound_adjacent_nodes(self, node: Node):
        edges = node.get_adjacent_edges()
        in_bound_adjacent_nodes = set()
        for edge in edges:
            in_bound_adjacent_nodes = in_bound_adjacent_nodes.union(
                edge.get_genisises()
            )
        if node in in_bound_adjacent_nodes:
            in_bound_adjacent_nodes.remove(node)
        return in_bound_adjacent_nodes

    def mark_nodes(self, nodes, flag_name: str):
        for node in nodes:
            node.flag = flag_name

    def mark_node(self, node: Node, flag_name: str):
        self.mark_nodes(set([node]), flag_name)

    def reset_nodes(self, nodes):
        self.mark_nodes(nodes, flag_name=None)

    def reset_node(self, node: Node):
        self.mark_node(node, flag=None)

    # def get_adj_nodes_with_criteria(self,node, criteria:function):
    #     pass

    def get_adjacent_nodes_with_flag(self, node: Node, flag_name: str):
        return set(
            [node for node in self.get_adjacent_nodes(node) if node.flag == flag_name]
        )

    def get_adjacent_nodes_without_flag(self, node: Node, flag_name: str):
        return set(
            [node for node in self.get_adjacent_nodes(node) if node.flag != flag_name]
        )

    def get_outbound_adjacent_nodes_with_flag(self, node: Node, flag_name: str):
        return set(
            [
                node
                for node in self.get_outbound_adjacent_nodes(node)
                if node.flag == flag_name
            ]
        )

    def get_outbound_adjacent_nodes_without_flag(self, node: Node, flag_name: str):
        return set(
            [
                node
                for node in self.get_outbound_adjacent_nodes(node)
                if node.flag != flag_name
            ]
        )

    def get_in_bound_adjacent_nodes_with_flag(self, node: Node, flag_name: str):
        return set(
            [
                node
                for node in self.get_in_bound_adjacent_nodes(node)
                if node.flag == flag_name
            ]
        )

    def get_in_bound_adjacent_nodes_without_flag(self, node: Node, flag_name: str):
        return set(
            [
                node
                for node in self.get_in_bound_adjacent_nodes(node)
                if node.flag != flag_name
            ]
        )

    def get_all_connected_nodes(self, node):
        self.reset_nodes(self.nodes)

        def explore_deep(node, node_set):
            to_explore = self.get_adjacent_nodes_without_flag(node, "EXPLORED")
            self.mark_nodes(to_explore, "EXPLORED")
            node_set.add(node)
            for new_node in to_explore:
                node_set = node_set.union(explore_deep(new_node, node_set))
            return node_set

        all_connected_nodes = explore_deep(node, set([node]))
        return all_connected_nodes

    def connection_exists(self, node0, node1):
        return node0 in self.get_all_connected_nodes(node1)

    def get_all_directionally_connected_nodes(self, node):
        self.reset_nodes(self.nodes)

        def explore_deep(node, node_set):
            to_explore = self.get_outbound_adjacent_nodes_without_flag(node, "EXPLORED")
            self.mark_nodes(to_explore, "EXPLORED")
            node_set.add(node)
            for new_node in to_explore:
                node_set = node_set.union(explore_deep(new_node, node_set))
            return node_set

        all_connected_nodes = explore_deep(node, set([node]))
        return all_connected_nodes

    def get_all_directionally_connected_edges(self, node):
        edges = set()
        for n in self.get_all_directionally_connected_nodes(node):
            edges = edges.union(n.outbound)
        return edges

    def directional_connection_exists(self, startnode, endnode):
        return endnode in self.get_all_directionally_connected_nodes(startnode)

    def shortest_path_directional(self, n0, n1):
        # returns distance, and path
        connected_nodes = self.get_all_directionally_connected_nodes(n0)
        if n1 not in connected_nodes:
            raise Exception("NO PATH EXISTS")
        for node in connected_nodes:
            node.flag = "UNSEEN"
            node.distance = "inf"
        n0.distance = 0

        current_node = n0

        while current_node is not n1:
            current_node.flag = "VISITED"
            adjacent_nodes = self.get_outbound_adjacent_nodes(current_node)
            for n in adjacent_nodes:
                relevant_edges = [
                    edge
                    for edge in self.edges
                    if edge.does_directionally_connect_nodes(current_node, n)
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

    def get_subgraph(self, nodes=None, edges=None):
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

    def find_cliques(self, size: int):
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
                for edge in node.get_adjacent_edges():
                    nodes = nodes.union(
                        set(node for node in edge.nodes if node in untested)
                    )
                untested.remove(node)
                if nodes:
                    nodes.remove(node)
                edges = set()
                for n in nodes:
                    for edge in n.get_adjacent_edges():
                        if (edge.node0 in nodes) and (edge.node1 in nodes):
                            edges.add(edge)
                local_graph = Graph(nodes=nodes, edges=edges)
                new_cliques = local_graph.find_cliques(size=size - 1)
                for clique in new_cliques:
                    clique.add(node)
                    cliques.append(clique)
        return cliques


def nodify(array) -> list:
    node_array = [[Node(val) for val in row] for row in array]
    return node_array
