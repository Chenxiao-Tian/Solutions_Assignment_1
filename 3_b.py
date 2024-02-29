# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 20:28:38 2024

@author: ct347
"""
import networkx as nx
import matplotlib.pyplot as plt
# Constructing a star network with 6 nodes (one center node and 5 peripheral nodes)
G_star = nx.star_graph(5)  # This creates a star graph with 6 nodes (0 is the center, 1-5 are the leaves)

# Calculating closeness centrality for the star network
closeness_centrality_star = nx.closeness_centrality(G_star)

# Printing the closeness centrality for the star network for verification
print("Star Network Closeness Centrality:", closeness_centrality_star)

# Plotting the star network
pos_star = nx.spring_layout(G_star)
plt.figure(figsize=(8, 6))
nx.draw(G_star, pos_star, with_labels=True, node_color='lightpink', node_size=700, edge_color='k', linewidths=1, font_size=15)
plt.title('Star Network Visualization')
plt.show()
