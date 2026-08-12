import heapq
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 4)],
    'F': [('G', 1)],
    'G': []
}
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 2,
    'F': 1,
    'G': 0
}
def astar(start, goal):
    pq = [(heuristic[start], 0, start)]
    visited = set()
    while pq:
        f, g, node = heapq.heappop(pq)
        if node == goal:
            print("Path Cost:", g)
            return
        if node not in visited:
            visited.add(node)
            for neighbour, cost in graph[node]:
                if neighbour not in visited:
                    g_new = g + cost
                    f_new = g_new + heuristic[neighbour]
                    heapq.heappush(pq, (f_new, g_new, neighbour))
astar('A', 'G')
