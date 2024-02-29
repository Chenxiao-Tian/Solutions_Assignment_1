import networkx as nx
import matplotlib.pyplot as plt
# Constructing a 5-node complete graph
G_complete = nx.complete_graph(5)

# Calculating degree centrality for the complete graph
degree_centrality_complete = nx.degree_centrality(G_complete)

# Calculating betweenness centrality for the complete graph
betweenness_centrality_complete = nx.betweenness_centrality(G_complete)

# Printing the centralities for the complete graph for verification
print("Complete Graph Degree Centrality:", degree_centrality_complete)
print("Complete Graph Betweenness Centrality:", betweenness_centrality_complete)

# Plotting the complete graph
pos_complete = nx.spring_layout(G_complete)
plt.figure(figsize=(8, 6))
nx.draw(G_complete, pos_complete, with_labels=True, node_color='lavender', node_size=700, edge_color='k', linewidths=1, font_size=15)
plt.title('Complete Graph Visualization')
plt.show()
