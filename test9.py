import networkx as nx
import matplotlib.pyplot as plt

# Create a Barabasi-Albert graph with 10,000 nodes and m=3
G = nx.barabasi_albert_graph(10000, 3)

# Draw a subgraph of the first 100 nodes using NetworkX and Matplotlib
nx.draw(G.subgraph(range(100)), with_labels=False)
plt.show()
