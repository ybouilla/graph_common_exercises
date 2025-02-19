from graph_utils import displayGraph

# check if a graph has a cycle
def has_cycle(graph):
    adj = list(graph.values())

    visited = [False] * len(graph)
    stack = set()
    print(adj)
    for source in range(len(adj)):
        is_cycle = is_node_in_cycle(adj, source, visited, stack)
        stack.remove(source )
        if is_cycle:
            return True
    return is_cycle


def is_node_in_cycle(adj, node, visited, stack):
    visited[node] = True
    stack.add(node)
    print(adj[node-1])
    for n in adj[node-1]:
        if not visited[n-1]:
            contains_cycle = is_node_in_cycle(adj, n-1, visited, stack)
            if contains_cycle:
                return True
        if node in stack:
            return True
    else: 
        return False


graph = {
    1: [2, 4],
    2: [3],
    3: [3],
    4: [5],
    5: [2]
}

print("HAS cycle")
print(has_cycle(graph))
displayGraph(graph, from_graph=True)