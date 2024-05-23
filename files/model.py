import networkx as nx

class Model(object):
	"""
	Base class for various system models.
	"""

	def __init__(self, directed=True, multi=True):
		"""
		Empty LOMAP Model object constructor.
		"""
		self.init = dict()
		self.name = 'Unnamed system model'
		self.final = set()
		if directed:
			if multi:
				self.g = nx.MultiDiGraph()
			else:
				self.g = nx.DiGraph()
		else:
			if multi:
				self.g = nx.MultiGraph()
			else:
				self.g = nx.Graph()
		self.directed = directed
		self.multi = multi

	def nodes_w_prop(self, propset):
		"""
		Returns the set of nodes with given properties.
		"""
		nodes_w_prop = set()
		for node,data in self.g.nodes(data=True):
			if propset <= data.get('prop',set()):
				nodes_w_prop.add(node)
		return nodes_w_prop

	def size(self):
		return (self.g.number_of_nodes(), self.g.number_of_edges())

	def visualize(self, edgelabel=None, draw='pygraphviz'):
		"""
		Visualizes a LOMAP system model
		"""
		if draw == 'pygraphviz':
			nx.view_pygraphviz(self.g, edgelabel)
		elif draw == 'matplotlib':
			pos = nx.spring_layout(self.g)
			nx.draw(self.g, pos=pos)
			nx.draw_networkx_labels(self.g, pos=pos)
		else:
			raise ValueError('Expected parameter draw to be either:'
							 + '"pygraphviz" or "matplotlib"!')
