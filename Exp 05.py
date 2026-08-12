import heapq
graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['E'],
    'C': [],
    'D': ['G'],
    'E': ['G'],
    'G': []
}
heuristic = {
    'S': 7,
    'A': 6,
    'B': 2,
    'C': 5,
    'D': 1,
    'E': 1,
    'G': 0
}
def greedy(start, goal):
    visited = set()
    pq = [(heuristic[start], start)]
    while pq:
        h, node = heapq.heappop(pq)
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            if node == goal:
                print("\nGoal Found")
                return
            for neighbour in graph[node]:
                if neighbour not in visited:
                    heapq.heappush(pq, (heuristic[neighbour], neighbour))
greedy('S', 'G')
