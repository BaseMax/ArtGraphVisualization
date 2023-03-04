import networkx as nx
import matplotlib.pyplot as plt

# Create a Krackhardt Kite graph
# Krackhardt Kite Graph
G = nx.krackhardt_kite_graph()

# Draw the graph using NetworkX and Matplotlib
nx.draw(G, with_labels=True)
plt.show()
