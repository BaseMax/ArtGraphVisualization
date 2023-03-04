import networkx as nx
import matplotlib.pyplot as plt

# Create a random regular graph with 10,000 nodes and degree 4
G = nx.random_regular_graph(4, 10000)

# Draw a subgraph of the first 100 nodes using NetworkX and Matplotlib
nx.draw(G.subgraph(range(100)), with_labels=False)
plt.show()
