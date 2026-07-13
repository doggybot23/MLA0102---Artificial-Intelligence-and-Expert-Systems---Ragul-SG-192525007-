from collections import deque

def bfs_explore(graph, start_node):
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)
    
    traversal_order = []

    while queue:
        current_node = queue.popleft()
        traversal_order.append(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return traversal_order

building_graph = {
    'Entrance': ['Room A', 'Room B'],
    'Room A': ['Entrance', 'Room C', 'Room D'],
    'Room B': ['Entrance', 'Room E'],
    'Room C': ['Room A'],
    'Room D': ['Room A'],
    'Room E': ['Room B']
}

print(bfs_explore(building_graph, 'Entrance'))