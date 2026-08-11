from heapq import heappush, heappop

graph = {
    'S': [('A', 2)],
    'A': [('B', 4), ('D', 6), ('E', 4)],
    'B': [('C', 3), ('E', 2), ('G', 6)],
    'C': [('G', 2)],
    'D': [('E', 3)],
    'E': [('F', 4)],
    'F': [('G', 1)],
    'G': []
}

heuristic = {
    'S': 8,
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 6,
    'E': 3,
    'F': 1,
    'G': 0
}

def astar(start, goal):
    pq = []
    heappush(pq, (heuristic[start], 0, start, [start]))
    visited = set()

    while pq:
        f, g, node, path = heappop(pq)

        if node == goal:
            print("Optimal Path:", " -> ".join(path))
            print("Total Cost:", g)
            return

        if node in visited:
            continue

        visited.add(node)

        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                heappush(pq, (new_f, new_g, neighbor, path + [neighbor]))

astar('S', 'G')
