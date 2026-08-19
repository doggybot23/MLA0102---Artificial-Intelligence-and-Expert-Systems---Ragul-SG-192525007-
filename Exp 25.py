import heapq

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 3,
    'E': 2,
    'F': 4,
    'G': 0
}

def best_first_search(start, goal):
    queue = [(heuristic[start], start, [start])]
    visited = set()

    while queue:
        h, node, path = heapq.heappop(queue)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            return path

        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(
                    queue,
                    (heuristic[neighbor], neighbor, path + [neighbor])
                )

    return None

path = best_first_search('A', 'G')
print("Path:", path)
