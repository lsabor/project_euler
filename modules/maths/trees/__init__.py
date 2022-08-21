# This module holds tree functions


class Node:
    def __init__(self, value=None, parent=None, children=None):
        self.value = value
        self.parent = parent
        self.children = [] if children is None else children
        self.depth = self.update_depth()

    def __repr__(self):
        return f"{self.parent_value()} <- **{self.value}** -> {self.children_values()}"

    def update_depth(self):
        self.depth = 0 if not self.parent else self.parent.depth + 1
        return self.depth

    def add_child(self, node):
        self.children.append(node)

    def children_values(self):
        return [x.value for x in self.children]

    def parent_value(self):
        if self.parent is not None:
            return self.parent.value
        return None

    # def serialize(self):
    #     node_dict = {
    #         'value'   : self.value,
    #         'children': [c.serialize() for c in self.children if c is not None],
    #     }
    #     return json.dumps(node_dict)


class Tree:
    display_depth = 10

    def __init__(self, first_node):
        self.head = first_node.__class__(first_node.initial_value)
        self.node_list = self.nodes()
        self.value_list = self.values()
        self.attach_node(first_node)

    def __repr__(self):
        i = 0
        rep = ""
        display_list = [self.head]
        while i < Tree.display_depth and display_list:
            rep += f"\nTree Depth {i}:"
            next_display_list = []
            for node in display_list:
                rep += "\n\t\t" + node.__repr__()
                next_display_list += node.children
            display_list = next_display_list
            i += 1
        return rep

    def display_full(self):
        raise NotImplementedError
        rep = ""
        display_list = [self.head]
        while display_list:
            rep += f"\nTree Depth :"
            next_display_list = []
            for node in display_list:
                rep += "\n\t\t" + node.__repr__()
                next_display_list += node.children
            display_list = next_display_list
        print(rep)

    def nodes(self):
        nodes = []
        node_list = [self.head]
        while node_list:
            nodes += node_list
            next_node_list = []
            for node in node_list:
                next_node_list += node.children
            node_list = next_node_list
        return nodes

    def values(self):
        return [node.value for node in self.node_list]

    def find_node_by_value(self, value) -> Node:
        if value in self.value_list:
            return self.node_list[self.value_list.index(value)]
        return None

    def attach_node(self, node):
        if node.value in self.value_list:
            return
        new_nodes = [node]
        attach_value = node.get_parent_value()
        attach_node = self.find_node_by_value(attach_value)
        while attach_node is None:
            new_node = node.__class__(attach_value)
            new_nodes.append(new_node)
            self.mate_nodes(node, new_node)
            node = new_node
            attach_value = node.get_parent_value()
            attach_node = self.find_node_by_value(attach_value)
        self.mate_nodes(node, attach_node)
        new_nodes = list(reversed(new_nodes))
        for node in new_nodes:
            node.update_depth()
        self.node_list += new_nodes
        self.value_list += [node.value for node in new_nodes]

    def attach_node_from_value(self, value):
        new_node = self.head.__class__(value)
        self.attach_node(new_node)

    def mate_nodes(self, child_node, parent_node):
        parent_node.add_child(child_node)
        child_node.parent = parent_node

    def max_depth(self):
        return

    # def serialize(self):
    #     serialization = self.head.serialize()
    #     return json.dumps(serialization)

    # @classmethod
    # def unserialize(self,tree_json):
    #     tree_dict = json.loads(tree_json)


class Collatz(Node):
    name = "Collatz"

    def __init__(self, value=1):
        self.initial_value = 1
        super().__init__(value=value)

    def get_parent_value(self):
        n = self.value
        return n // 2 if n % 2 == 0 else 3 * n + 1

    # @classmethod
    # def unserialize(node_json):
    #     node_dict = json.loads(node_json)
    #     return Collatz(**node_dict)
