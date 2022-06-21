import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pylab
import time

G = nx.DiGraph(directed=True)

G.add_edges_from([('A', 'B'),('B','C'),('B','D'), ('C', 'E')], weight=10)
G.add_edges_from([('A','C'),('A','D'),('C','D'),('D','E')], weight=5)
G.add_edges_from([('E','E')], weight=3)


val_map = {'A': 1.0,
           'B': 0.5714285714285714,
           'C': 0.5714285714285714,
           'D': 0.3,
           'E': 0.3}
start = time.time()

weights = {}
for edge in G.edges:
    weight = G.get_edge_data(edge[0], edge[1])['weight']
    if weight not in weights:
        weights[weight] = [edge]
    else:
        weights[weight] += [edge]

sorted_weights = sorted(weights.keys(), reverse = True)
sorted_edges = []
for i in sorted_weights:
    sorted_edges.extend(weights[i])

nodelist = list(G.nodes)
edgelist = {}

while nodelist != [] and sorted_edges != []:
    edge = sorted_edges.pop(0)
    if (edge[0] not in nodelist) and (edge[1] not in nodelist):
        continue
    else:
        edgelist[edge]=G.get_edge_data(edge[0], edge[1])['weight']
        if edge[0] in nodelist:
            nodelist.pop(nodelist.index(edge[0]))
        if edge[1] in nodelist:
            nodelist.pop(nodelist.index(edge[1]))



values = [val_map.get(node, 0.25) for node in G.nodes()]

edge_labels=dict([((u,v,),d['weight'])
                 for u,v,d in G.edges(data=True)])
red_edges = list(edgelist.keys())
edge_colors = ['black' if not edge in red_edges else 'red' for edge in G.edges()]

pos=nx.spring_layout(G)
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
nx.draw(G,pos, node_color = values, node_size=1500,edge_color=edge_colors,edge_cmap=plt.cm.Reds)
#nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), 
#                       node_color = values, node_size = 500)
nx.draw_networkx_labels(G, pos)
end = time.time()
print(end-start)
pylab.show()