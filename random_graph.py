import networkx as nx
import random

from graph import ER


def random_graph(n):
	""" vytvoří náhdný graf o n nodech a přetvoří ho do datové struktury grafu pomocí slovníku"""
	p = 0.15 if n<80 else 0.05
	G = ER(n, p)
	a = nx.convert.to_dict_of_lists(G)

	dict_values = a.items()

	new_a = {str(key):value for key, value in dict_values} 

	dict_values2 = new_a.items()

	for key, value in dict_values2:
	    new_a[key] = [(str(v),random.randint(1,2)) for v in value]

	return new_a

