import timeit
from timeit import repeat

from random_graph import random_graph

from random_dict_plot import draw_random_graph

from graph import ER

test_array = [i for i in range(1,101) if i % 10 == 0]

def time_random_graph():
	""" otestuje rychlost vytvoření náhodného grafu a přetvooření do datové struktury grafu """
	for i in test_array:
		time = timeit.timeit(f"random_graph({i})", globals=globals(), number=100)/100
		print(f"vytvoření náhodného grafu a přetvooření do datové struktury grafu o {i} nodech trvá {time:.7f} s ")
		print()


def time_random_dict_plot():
	""" otestuje rychlost nalezení cesty v náhodném grafu """
	for i in test_array:
		time = timeit.timeit(f"draw_random_graph({i})", globals=globals(), number=1)
		print(f"nalezení cesty v náhodném grafu o {i} nodech trvá {time:.7f} s ")
		print()


test_ER_dict = {i:( 0.15 if i<80 else 0.05) for i  in range(1,101) if i % 10 == 0}

def time_ER():
	""" otestuje rychlost vythoření náhodného grafu """
	for key, value in test_ER_dict.items():
		time = timeit.timeit(f"ER({key},{value})", globals=globals(), number=100)/100
		print(f"vythoření náhodného grafu o {key} nodech trvá {time:.7f} s ")
		print()


if __name__ == "__main__":
	print("TESTOVÁNÍ ČASU time_random_graph()")
	time_random_graph()
	print("""



	TESTOVÁNÍ ČASU time_random_dict_plot()
		""")
	time_random_dict_plot()
	print("""



	TESTOVÁNÍ ČASU time_ER()
		""")
	time_ER()