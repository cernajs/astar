
class Astar:
	""" základní třída implementující a* algoritmus na grafu v podobě slovníku"""
	def __init__(self, nodes, start_node, end_node):

		self.nodes = nodes
		self.start_node = start_node
		self.end_node = end_node

		self.unvisited = set([start_node])
		self.visited = set([])

		self.g_cost = {}
		self.g_cost[start_node] = 0

		self.parents = {}
		self.parents[start_node] = self.start_node

	def neighborou(self,n):
		return self.nodes[n]

	def heurestic(self, n):
		nodes = {
				key: 1 for key in self.nodes.keys()
				}

		return nodes[n]

	def search(self):
		while len(self.unvisited) > 0:
			n = None

			for node in self.unvisited:
				if n == None or self.g_cost[node] + self.heurestic(node) < self.g_cost[n] + self.heurestic(n):
					n = node

			if n == self.end_node:
				path = []

				while self.parents[n] != n:
					path.append(n)
					n = self.parents[n]

				path.append(self.start_node)

				path.reverse()

				return path


			for x, cost in self.neighborou(n):
				if x not in self.visited and x not in self.unvisited:
					self.unvisited.add(x)
					self.parents[x] = n 
					self.g_cost[x] = self.g_cost[n] + cost

				else:
					if self.g_cost[x] > self.g_cost[n] + cost:
						self.g_cost[x] = self.g_cost[n] + cost
						self.parents[x] = n

						if x in self.visited:
							self.visited.remove(x)
							self.unvisited.add(x)

			self.unvisited.remove(n)
			self.visited.add(n)

		return None





