import networkx as nx
import matplotlib.pyplot as plt

with open('/Users/willberritt/Downloads/facebook_combined.txt', 'r') as f:
    data = nx.read_edgelist(f, delimiter=' ', create_using=nx.Graph(), nodetype=int)

diameter = nx.diameter(data)
num_nodes = data.number_of_nodes()
num_edges = data.number_of_edges()
density = nx.density(data)

print(f"diameter: {diameter}")
print(f"nodes: {num_nodes}")
print(f"edges: {num_edges}")
print(f"density: {density}")

plt.figure()
nx.draw(data, node_size=5)
plt.show()