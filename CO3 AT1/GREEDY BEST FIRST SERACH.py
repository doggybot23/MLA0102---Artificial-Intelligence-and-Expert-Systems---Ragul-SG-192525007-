from queue import PriorityQueue

# Graph representation
graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': ['G'],
    'G': []
}

# Heuristic values
heuristic = {
    'S': 10,
    'A': 8,
    'B': 6,
    'C': 5,
    'D': 7,
    'E': 3,
    'F': 2,
    'G': 0
}

def greedy_best_first_search(start, goal):
    pq = PriorityQueue()
    pq.put((heuristic[start], start))

    visited = set()
    parent = {start: None}

    print("Node Expansion Order:")

    while not pq.empty():
        h, current = pq.get()

        if current in visited:
            continue

        print(current, end=" ")
        visited.add(current)

        if current == goal:
            print("\nGoal Found!")
            break

        for neighbor in graph[current]:
            if neighbor not in visited:
                parent[neighbor] = current
                pq.put((heuristic[neighbor], neighbor))

    # Reconstruct path
    path = []
    node = goal

    while node is not None:
        path.append(node)
        node = parent.get(node)

    path.reverse()

    print("\nPath:")
    print(" -> ".join(path))


# Driver Code
start = 'S'
goal = 'G'

greedy_best_first_search(start, goal)
