import timeit
import string
import matplotlib.pyplot as plt
import networkx as nx
from itertools import combinations
from random import random, randint


from astar_graph import  Astar


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


n = 50
p = 0.1
G = ER(n, p)
a = nx.convert.to_dict_of_lists(G)


dict_values = a.items()

new_a = {str(key):value for key, value in dict_values} 


dict_values2 = new_a.items()

for key, value in dict_values2:
    new_a[key] = [(str(v),random.randint(1,3)) for v in value]
    

astar = Astar(new_a,"0", "48")
print(astar.search())

shortest_path = [int(i) for i in astar.search()]
print(shortest_path)
node_colors = ["blue" if n in shortest_path else "red" for n in G.nodes()]


pos = nx.spring_layout(G)
nx.draw_networkx(G, pos, node_color=node_colors)


for i in range(0,len(shortest_path)):
    if i+1 == len(shortest_path):
        break
    nx.draw_networkx_edges(G,pos,
    edgelist=[(shortest_path[i],shortest_path[i+1])],
    edge_color="blue",width=2)

    
plt.show()
