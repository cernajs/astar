import networkx as nx
from itertools import combinations
from random import random

"""
nodes = {
    "A": [("B", 2), ("D", 3)],
    "B": [("A", 2), ("D", 5), ("C", 2)],
    "C": [("B", 2), ("F", 1)],
    "D": [("A", 3), ("B", 5), ("E", 8),("G", 7)],
    "E": [("D", 8), ("G", 5)],
    "F": [("C", 1), ("H", 3)],
    "G": [("E", 5), ("D", 7), ("H", 2)],
    "H": [("G", 2), ("F", 3)]
}
"""

def ER(n, p):
    V = set([v for v in range(n)])
    E = set()
    for combination in combinations(V, 2):
        a = random()
        if a < p:
            E.add(combination)

    g = nx.Graph()
    g.add_nodes_from(V)
    g.add_edges_from(E)

    return g


print(ER(10,0.5) == True)