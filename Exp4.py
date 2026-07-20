import heapq
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
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
def best_first(start, goal):
    visited = set()
    pq = [(heuristic[start], start)]
    while pq:
        h, node = heapq.heappop(pq)
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            if node == goal:
                print("\nGoal Reached")
                return
            for neighbour in graph[node]:
                if neighbour not in visited:
                    heapq.heappush(pq, (heuristic[neighbour], neighbour))
best_first('A', 'G')
