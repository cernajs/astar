import timeit

import_module = "from astar import Astar"
test_code = """
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
a = Astar(nodes,"A","H")
a.search()
"""

print(timeit.timeit(stmt=test_code, setup=import_module))