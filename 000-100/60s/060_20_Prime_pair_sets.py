"""
## Prime pair sets

Problem 60

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.


Link: https://projecteuler.net/problem=60

Date solved:  
2022/07/28   
w/ George Jeffreys
"""

# TODO: BROKEN

ANSWER = 26033

# imports

from maths.sequences import PrimesSeq
from maths.graphs import Node, Edge, Graph
from maths.primes import isPrime

# solution

P = PrimesSeq()
ps = set(P.seq)

threshold = 5


def is_prime_pair_set(p1, p2):
    return isPrime(int(str(p1) + str(p2))) and isPrime(int(str(p2) + str(p1)))


def find_prime_pair_group(threshold):
    nodes = []
    for p in P.seq[1:]:
        # go through with primes one at a time
        new_node = Node(p)
        nodes.append(new_node)
        edges = set()
        for node in nodes:
            if node.value == new_node.value:
                pass
            elif is_prime_pair_set(node.value, new_node.value):
                edges.add(Edge(node, new_node))

        graph = Graph(edges=edges)
        if new_node in graph.nodes:
            graph.remove(new_node)

        if cliques := graph.findCliques(size=threshold - 1):
            return [clique.union(set([new_node])) for clique in cliques]


def solution(bypass=False):
    if bypass:
        return ANSWER

    clique = find_prime_pair_group(threshold)[0]
    return sum([node.value for node in clique])


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution(bypass=False)
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
