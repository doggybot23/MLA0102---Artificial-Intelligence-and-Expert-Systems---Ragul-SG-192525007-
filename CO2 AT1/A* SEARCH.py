from queue import PriorityQueue

# Weighted graph
graph = {
    'S': [('A', 1), ('B', 4)],
    'A': [('C', 2), ('D', 5)],
    'B': [('D', 1)],
    'C': [('G', 5)],
    'D': [('G', 3)],
    'G': []
}

# Heuristic values
heuristic = {
    'S': 7,
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 2,
    'G': 0
}

def a_star(start, goal):
    open_list = PriorityQueue()
    open_list.put((heuristic[start], start))

    g = {start: 0}
    parent = {start: None}
    visited = set()

    print("Expanded Nodes:")
    print("Node\tg(n)\th(n)\tf(n)")

    while not open_list.empty():
        f, current = open_list.get()

        if current in visited:
            continue

        visited.add(current)

        print(f"{current}\t{g[current]}\t{heuristic[current]}\t{g[current] + heuristic[current]}")

        if current == goal:
            break

        for neighbor, cost in graph[current]:
            new_g = g[current] + cost

            if neighbor not in g or new_g < g[neighbor]:
                g[neighbor] = new_g
                parent[neighbor] = current
                f_value = new_g + heuristic[neighbor]
                open_list.put((f_value, neighbor))

    # Construct path
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent[node]

    path.reverse()

    print("\nOptimal Path:")
    print(" -> ".join(path))
    print("Total Cost =", g[goal])


# Driver Code
a_star('S', 'G')
