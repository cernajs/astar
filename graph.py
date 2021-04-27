import networkx as nx
from itertools import combinations
from random import random


def ER(n, p):
    """ vytvoří náhodny graf o n nodech"""
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
