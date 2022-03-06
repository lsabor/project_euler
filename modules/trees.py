# This module holds tree functions

import picke


class Node:

    def __init__(self,value = None):
        self.value = value

    def __repr__(self):
        return self.value

class Node_Upward(Node):

    def __init__(self,value = None):
        super().__init__(value)
        self.parent = None

class Node_Immovable(Node_Upward):
    
    def __init__(self,value = None):
        super().__init__(value)
        self.dist     = self.distance
        self.children = []
    
    def distance(self):
        dist = 0
        if self.parent is not None:
            dist = 1 + self.parent.dist
        return dist



class Tree:

    def __init__(self,head = None):
        self.head = head


class Tree_Unchanging(Tree):

    def __init__(self,head = None):
        super().__init__(head)
        self.nodes = {head.value: head}

    def attach(self,node: Node) -> Tree:
        next_val = self.get_next_value(node)
        if next_val in self.nodes:
            parent_node = self.nodes[next_val]
            self.connect_nodes(node,parent_node)
        else:
            next_node = Node_Immovable(next_val)
            self.connect_nodes(node,next_node)
            self.attach(next_node)
    
    def connect_nodes(self,child_node,parent_node):
        child_node.parent = parent_node
        parent_node.children.append(child_node)

    def get_next_value(node):
        pass # define this in child class



class Collatz(Tree_Unchanging):

    

    def __init__(self):
        super().__init__(Node_Immovable(value = 1))
        self.name = "Collatz"

    def get_next_value(node):
        n = node.value
        return n/2 if n%2==0 else 3*n+1






