def dfs_explore(graph, current_node, visited=None, traversal_order=None):
    if visited is None:
        visited = set()
    if traversal_order is None:
        traversal_order = []

    visited.add(current_node)
    traversal_order.append(current_node)

    for neighbor in graph[current_node]:
        if neighbor not in visited:
            dfs_explore(graph, neighbor, visited, traversal_order)
            
    return traversal_order

cave_graph = {
    'Cave Entrance': ['Tunnel 1', 'Tunnel 2'],
    'Tunnel 1': ['Cave Entrance', 'Deep Cavern A', 'Deep Cavern B'],
    'Tunnel 2': ['Cave Entrance', 'Underground Lake'],
    'Deep Cavern A': ['Tunnel 1', 'Dead End 1'],
    'Deep Cavern B': ['Tunnel 1'],
    'Underground Lake': ['Tunnel 2'],
    'Dead End 1': ['Deep Cavern A']
}

print(dfs_explore(cave_graph, 'Cave Entrance'))