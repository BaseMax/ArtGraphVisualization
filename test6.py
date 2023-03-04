import networkx as nx
import matplotlib.pyplot as plt

# Create a random geometric graph with 20 nodes
G = nx.random_geometric_graph(20, 0.2)

# Draw the graph using NetworkX and Matplotlib
pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, pos, with_labels=True)
plt.show()
