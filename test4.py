import networkx as nx
import matplotlib.pyplot as plt

# Create a bipartite graph with 6 nodes and 5 edges
G = nx.Graph()
G.add_nodes_from(['A', 'B', 'C', 'D'], bipartite=0)
G.add_nodes_from([1, 2, 3], bipartite=1)
G.add_edges_from([('A', 1), ('B', 1), ('C', 2), ('D', 3), ('D', 2)])

# Draw the graph using NetworkX and Matplotlib
pos = nx.spring_layout(G)
top_nodes = {'A', 'B', 'C', 'D'}
bottom_nodes = set(G) - top_nodes
nx.draw_networkx_nodes(G, pos, nodelist=top_nodes, node_color='r')
nx.draw_networkx_nodes(G, pos, nodelist=bottom_nodes, node_color='b')
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos)
plt.show()
