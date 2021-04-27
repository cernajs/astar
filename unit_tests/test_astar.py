import unittest
import sys
sys.path.append("..")


from astar import Astar


class TestAstar(unittest.TestCase):
	""" otestuje třídu Astar """

	def test_astar1(self):

		nodes1 = {
    	"A": [("B", 2), ("D", 3)],
    	"B": [("A", 2), ("D", 5), ("C", 2)],
    	"C": [("B", 2), ("F", 1)],
    	"D": [("A", 3), ("B", 5), ("E", 8),("G", 7)],
    	"E": [("D", 8), ("G", 5)],
    	"F": [("C", 1), ("H", 3)],
    	"G": [("E", 5), ("D", 7), ("H", 2)],
    	"H": [("G", 2), ("F", 3)]
		}

		astar1 = Astar(nodes1,"A","H")
		result1 = astar1.search()

		self.assertEqual(result1,['A', 'B', 'C', 'F', 'H'])

	def test_astar2(self):

		nodes2 = {
	    "A": [("B", 2), ("E", 2)],
	    "B": [("A", 2), ("C", 2)],
	    "C": [("B", 2), ("D", 2)],
	    "D": [("C", 2), ("G", 2)],
	    "E": [("A", 2), ("J", 3)],
	    "F": [("B", 2), ("K", 2), ("G", 2)],
	    "G": [("F", 2), ("D", 2), ("L", 4), ("H", 3)],
	    "H": [("G", 3), ("I", 2)],
	    "I": [("H", 2), ("M", 3)],
	    "J": [("E", 3), ("O", 4)],
	    "K": [("F", 2), ("O", 2)],
	    "L": [("G", 4), ("M", 1),("P", 5)],
	    "M": [("I", 3), ("L", 1)],
	    "O": [("K", 2), ("J", 4)],
	    "P": [("L", 5)]
		}

		astar2 = Astar(nodes2,"A","P")
		result2 = astar2.search()
	
		self.assertEqual(result2,['A', 'B', 'C', 'D', 'G', 'L', 'P'])

if __name__ == '__main__':
	unittest.main()