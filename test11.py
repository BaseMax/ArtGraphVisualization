import random
import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()
G.add_nodes_from(range(10))
G.add_edges_from([(0,1), (1,2), (2,3), (3,4), (4,5), (5,6), (6,7), (7,8), (8,9), (9,0)])

# Set random colors for nodes and edges
node_colors = [random.choice(['red', 'blue', 'green']) for _ in range(len(G.nodes()))]
edge_colors = [random.choice(['red', 'blue', 'green']) for _ in range(len(G.edges()))]

# Draw the graph with node and edge colors
nx.draw(G, with_labels=True, node_color=node_colors, edge_color=edge_colors)
plt.show()
