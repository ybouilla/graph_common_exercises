import networkx as nx
import matplotlib.pyplot as plt


def displayGraph(edges, from_graph = False):
  if from_graph:
    tmp_edges = []
    for n, eds in edges.items():
        for ed in eds:
            tmp_edges.append([n, ed])
  edges = tmp_edges
  G=nx.Graph()
  G.add_edges_from(edges)
  nx.draw_networkx(G)
  plt.show()
  return

def displayGraphwWeights(adj):
    G=nx.Graph()
    edges = []
    for u in range(len(adj)):
        for v in range(len(adj[u])):
            if adj[u][v] > 0:
               edges.append((u, v, adj[u][v]))
    G.add_weighted_edges_from(edges)
    nx.draw_networkx(G)
    plt.show()