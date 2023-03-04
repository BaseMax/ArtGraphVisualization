import networkx as nx
import matplotlib.pyplot as plt

# Create a weighted graph with 5 nodes and 5 edges
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4, 5])
G.add_weighted_edges_from([(1,2,3), (2,3,5), (3,4,7), (4,5,9), (5,1,11)])

# Draw the graph using NetworkX and Matplotlib
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, edge_color='b', width=2, node_size=500, node_color='w')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()
