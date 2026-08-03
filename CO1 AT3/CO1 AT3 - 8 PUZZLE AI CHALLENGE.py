# 8-Puzzle AI Challenge
# Solve using A* Search Algorithm (Minimum Moves)

from heapq import heappush, heappop

GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

# Example Initial State
START = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

def heuristic(state):
    """Manhattan Distance"""
    distance = 0
    for i, value in enumerate(state):
        if value == 0:
            continue
        goal_pos = GOAL.index(value)
        x1, y1 = divmod(i, 3)
        x2, y2 = divmod(goal_pos, 3)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

def neighbors(state):
    index = state.index(0)
    x, y = divmod(index, 3)

    moves = [(-1,0), (1,0), (0,-1), (0,1)]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_index = nx * 3 + ny
            new_state = list(state)
            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
            yield tuple(new_state)

def print_board(state):
    for i in range(0, 9, 3):
        print(state[i], state[i+1], state[i+2])
    print()

def a_star(start):
    pq = []
    heappush(pq, (heuristic(start), 0, start, []))
    visited = set()

    while pq:
        f, g, state, path = heappop(pq)

        if state in visited:
            continue

        visited.add(state)

        if state == GOAL:
            return path + [state]

        for next_state in neighbors(state):
            if next_state not in visited:
                heappush(
                    pq,
                    (g + 1 + heuristic(next_state),
                     g + 1,
                     next_state,
                     path + [state])
                )

    return None

solution = a_star(START)

if solution:
    print("Solution Found!\n")

    for step, state in enumerate(solution):
        print(f"Move {step}")
        print_board(state)

    print("Minimum Moves:", len(solution) - 1)

else:
    print("No solution exists.")
