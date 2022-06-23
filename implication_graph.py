#TIZIANO FINIZZI
import networkx as nx
import matplotlib.pyplot as plt

options = {
    'node_color': 'lightblue',
    'node_size': 300,
    'width': 3,
    'with_labels':True,
}


class ImplicationGraph:
    def __init__(self, formula):
    	self.g = nx.DiGraph()
    	for i in range(0,len(formula)):
    		#i-th clause
    		c=formula[i]
    		#create new graph nodes
    		self.g.add_node(c[0])
    		self.g.add_node(c[1])
    		self.g.add_node(-c[0])
    		self.g.add_node(-c[1])
    		#add new edges to implication graph
    		self.g.add_edge(c[0],-c[1])
    		self.g.add_edge(-c[0],c[1])
		
    def literals(self):
    	for l in self.g.nodes:
        	yield l
    def successors(self, literal):
      	for l in self.g.successors(literal):
      		yield l

    def draw(self):
        nx.draw(self.g, **options)
        plt.show()
'''
	def draw_sccs(self, sccs):
        # Optional
        # Delete this method if you decide not to implement it
        # Delete these comments if you decide to implement it
        """
        Draws the Strongly Connected Components graph
        given a collection of lists of literals
        representing the SCC.
        """
'''
    





	



	


