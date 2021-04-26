import unittest
import sys
import random
sys.path.append("..")


from graph import ER

class TestAstar(unittest.TestCase):

	def test_astar(self):

		n = random.randint(10,100)
		p = random.choice([0.05,0.1])

		result = ER(n,p) == True

		self.assertFalse(result)

if __name__ == '__main__':
	unittest.main()