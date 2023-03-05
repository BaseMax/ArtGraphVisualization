import networkx as nx
import matplotlib.pyplot as plt

# Create a random graph with 50 nodes
G = nx.fast_gnp_random_graph(50, 0.2)

# Generate a layout using the spring layout algorithm
pos = nx.spring_layout(G)

# Draw the graph using the layout and default settings
nx.draw(G, pos)

# Add a title to the plot
plt.suptitle("Generated using the fast_gnp_random_graph() function from NetworkX", fontsize=12)

# Display the plot
plt.show()
