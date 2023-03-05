import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Create a random graph with 10,000 nodes and 50,000 edges
G = nx.gnm_random_graph(1000, 5000)

# Set random weights for the edges
weights = np.random.rand(len(G.edges))
nx.set_edge_attributes(G, dict(zip(G.edges, weights)), 'weight')

# Generate a layout using the spring layout algorithm
pos = nx.spring_layout(G)

# Assign colors to the nodes based on their degree
node_colors = np.array(list(dict(G.degree()).values()))
node_colors = (node_colors - node_colors.min()) / (node_colors.max() - node_colors.min())

# Assign colors to the edges based on their weight
edge_weights = nx.get_edge_attributes(G, 'weight')
edge_weights_norm = (np.array(list(edge_weights.values())) - min(edge_weights.values())) / (max(edge_weights.values()) - min(edge_weights.values()))
cmap = plt.cm.get_cmap('Blues')
edge_colors = cmap(edge_weights_norm)

# Draw the graph using the layout and color scheme
nx.draw(G, pos=pos, node_color=node_colors, edge_color=edge_colors, with_labels=False, node_size=5, width=0.5)

# Add a title and subtitle to the plot
plt.title("Random Graph with 10,000 Nodes and 50,000 Edges")
plt.suptitle("Generated using the gnm_random_graph() function from NetworkX")

# Display the plot
plt.show()
