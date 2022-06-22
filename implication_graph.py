#TIZIANO FINIZZI
import networkx as nx
import matplotlib.pyplot as plt
test_var=[[(1,-2),(1,2),(1,-3)],[(1,2),(2,-1),(-1,-2)],[(1,2),(2,-1),(1,-2),(-1,-2)]]
options = {
    'node_color': 'lightblue',
    'node_size': 300,
    'width': 3,
    'with_labels':True,
}
'''
# a OR b ===> (!a -> b) AND (!b -> a)
def convert_2sat_to_implication(f):
	g=[]
	for i in range(0,len(f)):
		c=f[i]
		g1=(-c[0],c[1])
		g2=(c[0],-c[1])
		g.append(g1)
		g.append(g2)
	return g #return a new formula with implications
'''
def create_graph(f):
	g = nx.DiGraph()
	for i in range(0,len(f)):
		#i-th clause
		c=f[i]
		#create new graph nodes
		g.add_node(c[0])
		g.add_node(c[1])
		g.add_node(-c[0])
		g.add_node(-c[1])
		#add new edges to implication graph
		g.add_edge(c[0],-c[1])
		g.add_edge(-c[0],c[1])
	return g

g=create_graph(test_var[2])

nx.relabel_nodes(g,{ x : str(x) if x>0 else f'!{-x}' for x in g})
nx.draw_spectral(g, **options)
plt.show()
	


