import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('G', 1)],
    'F': [('G', 3)],
    'G': []
}

def ucs(start, goal):
    pq = [(0, start)]
    visited = set()

    while pq:
        cost, node = heapq.heappop(pq)

        if node == goal:
            print("Minimum Cost:", cost)
            return

        if node not in visited:
            visited.add(node)

            for neighbour, weight in graph[node]:
                if neighbour not in visited:
                    heapq.heappush(pq, (cost + weight, neighbour))

ucs('A', 'G')
