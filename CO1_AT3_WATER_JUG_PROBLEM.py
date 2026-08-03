# Water Jug Puzzle (11L and 9L)
# Goal: Measure exactly 8 litres using BFS (minimum moves)

from collections import deque

CAP_A = 11
CAP_B = 9
GOAL = 8

def bfs():
    queue = deque()
    visited = set()

    start = (0, 0)
    queue.append((start, []))
    visited.add(start)

    while queue:
        (a, b), path = queue.popleft()

        # Goal check
        if a == GOAL or b == GOAL:
            return path + [(a, b)]

        next_states = []

        # Fill Jug A
        next_states.append(((CAP_A, b), "Fill Jug A"))

        # Fill Jug B
        next_states.append(((a, CAP_B), "Fill Jug B"))

        # Empty Jug A
        next_states.append(((0, b), "Empty Jug A"))

        # Empty Jug B
        next_states.append(((a, 0), "Empty Jug B"))

        # Pour A -> B
        transfer = min(a, CAP_B - b)
        next_states.append(((a - transfer, b + transfer), "Pour A -> B"))

        # Pour B -> A
        transfer = min(b, CAP_A - a)
        next_states.append(((a + transfer, b - transfer), "Pour B -> A"))

        for state, action in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [(action, state)]))

    return None

solution = bfs()

if solution:
    print("Minimum Move Solution:\n")
    print("Start State: (0, 0)")

    moves = 0
    for step in solution[:-1]:
        action, state = step
        moves += 1
        print(f"Move {moves}: {action} -> {state}")

    final_state = solution[-1]
    print("\nGoal Reached:", final_state)
    print("Total Moves:", moves)
else:
    print("No solution found.")
