import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph with 5 nodes and 5 edges
G = nx.DiGraph()
G.add_nodes_from([1, 2, 3, 4, 5])
G.add_edges_from([(1,2), (2,3), (3,4), (4,5), (5,1)])

# Draw the graph using NetworkX and Matplotlib
nx.draw(G, with_labels=True, arrows=True)
plt.show()
