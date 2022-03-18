# This module holds basic graph functions


class Node:
    
    def __init__(self,value=None):
        self.value = value

    def __repr__(self):
        return str(self.value)

class Edge:

    def __init__(self,length = 0,n1 = None,n2 = None):
        self.length = length
        self.n1 = n1
        self.n2 = n2

    def __repr__(self):
        return f'{self.n1} -{self.length if self.length else ""}> {self.n2}'


class Graph:

    def __init__(self,edges = None):
        self.edges = edges if edges else []

    def add_edge(self,edge):
        self.edges.append(edge)

    def __repr__(self):
        output = ''
        for edge in self.edges:
            output += f'{edge}\n'
        return output


