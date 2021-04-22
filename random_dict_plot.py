import matplotlib.pyplot as plt
import networkx as nx
import random

from graph import ER
from astar import  Astar


def draw_random_graph(n):
	p = 0.15 if n<80 else 0.05
	G = ER(n, p)
	a = nx.convert.to_dict_of_lists(G)

	dict_values = a.items()

	new_a = {str(key):value for key, value in dict_values} 

	dict_values2 = new_a.items()

	for key, value in dict_values2:
	    new_a[key] = [(str(v),random.randint(1,2)) for v in value]
	    

	astar = Astar(new_a,str(random.randint(0,n)), str(random.randint(0,n)))
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
 

draw_random_graph(200)