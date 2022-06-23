# TIZIANO FINIZZI
from re import A
import networkx as nx
import math
import matplotlib.pyplot as plt

options = {
    'node_color': 'lightblue',
    'node_size': 300,
    'width': 3,
    'with_labels': True,
}


class ImplicationGraph:
    def __init__(self, formula):
        self.g = nx.DiGraph()
        for i in range(0, len(formula)):
            # i-th clause
            c = formula[i]
            # create new graph nodes
            self.g.add_node(c[0])
            self.g.add_node(c[1])
            self.g.add_node(-c[0])
            self.g.add_node(-c[1])
            # add new edges to implication graph
            self.g.add_edge(-c[0], c[1])
            self.g.add_edge(-c[1], c[0])

    def literals(self):
        for l in self.g.nodes:
            yield l

    def successors(self, literal):
        for l in self.g.successors(literal):
            yield l

    def get_label_mapping(self):
        if len(self.g.nodes) <= 26:
            return {
                l: ("¬" if l < 0 else "") + chr(abs(l) + ord('a') - 1) for l in self.literals()
            }
        else:
            return {
                l: ("¬" if l < 0 else "") + f"{abs(l)}" for l in self.literals()
            }

    def draw(self):
        nx.draw_spectral(self.g, **options, labels=self.get_label_mapping())
        plt.show()

    def draw_sccs(self):
        """
        Draws the Strongly Connected Components graph
        given a collection of lists of literals
        representing the SCC.
        """
        from tarjan import tarjan
        sccs = tarjan(self)
        condensed = nx.condensation(self.g, sccs)
        literal_mapping = self.get_label_mapping()
        labels = {}
        for i, scc in enumerate(sccs):
            scc_label = ", ".join(map(lambda l: literal_mapping[l], scc))
            labels[i] = f"{{ {scc_label} }}"

        nx.draw(condensed, **options, labels=labels)
        plt.show()
