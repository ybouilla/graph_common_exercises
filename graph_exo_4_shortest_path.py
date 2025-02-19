from graph_utils import displayGraphwWeights

def djikstra(adj, s):
    # time complexity: O(nodes**2)
    # intialize distance to infinite
    dist = [float('inf') for _ in range(len(adj))]
    dist[s] = 0
    shortest_path_tree_set = [False] * len(adj)

    for itera in range(len(adj)):
        min_node = min_distance(adj, dist, shortest_path_tree_set)
        shortest_path_tree_set[min_node] = True

        for n in range(len(adj)):
            if adj[min_node][n] > 0 and not shortest_path_tree_set[n] \
                and dist[n]> dist[min_node] + adj[min_node][n]:
                dist[n] = dist[min_node] + adj[min_node][n]

    return dist

def min_distance(adj, dist, shortest_path_tree):
    """finds min distance from a set of nodes not included oij the shortest path"""
    min_dist = float('inf')
    for node in range(len(adj)):
        if dist[node] < min_dist  and not shortest_path_tree[node]:
            min_dist = dist[node]
            min_idx = node

    return min_idx

def print_solution(adj, dist):
        print("Vertex \t Distance from Source")
        for node in range(len(adj)):
            print(node, "\t\t", dist[node])


graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]

d = djikstra(graph, 0)
print(d)
print_solution(graph, d)

displayGraphwWeights(graph)