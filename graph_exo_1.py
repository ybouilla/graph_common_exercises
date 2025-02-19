from graph_utils import displayGraph

# largest component


graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 5, 6],
    4: [2],
    5: [3],
    6: [3],
    7: [8, 9, 10],
    8: [7],
    9: [7],
    10: [7],
    11: [12],
    12: [11]
}


def get_largest_component(graph):
    # uses DFS
    visited = [False] * len(graph)


    items = []
    adj = list(graph.values())
    print(adj)
    for i in range(len(graph)):
        item = []
        rec_dfs(adj, visited, i, item)
        items.append(len(item))
    return max(items)

def rec_dfs(adj, visited, source, item):
    
    visited[source] = True
    item.append(source)
    for i in adj[source]:
        print(i, visited)
        if not visited[i-1]:
            rec_dfs(adj, visited, i-1, item)


largest = get_largest_component(graph)
print("largest component", largest)


displayGraph(graph, from_graph=True)
