# AI Maze Escape - Shortest Path using Breadth First Search (BFS)

from collections import deque

# Maze:
# S = Start
# G = Goal
# # = Wall
# . = Free Path

maze = [
    ['S', '.', '.', '#', '.', '.'],
    ['#', '#', '.', '#', '.', '#'],
    ['.', '.', '.', '.', '.', '.'],
    ['.', '#', '#', '#', '#', '.'],
    ['.', '.', '.', '.', 'G', '.']
]

rows = len(maze)
cols = len(maze[0])

# Find Start and Goal
for i in range(rows):
    for j in range(cols):
        if maze[i][j] == 'S':
            start = (i, j)
        elif maze[i][j] == 'G':
            goal = (i, j)

# Possible movements: Up, Down, Left, Right
directions = [(-1,0), (1,0), (0,-1), (0,1)]

queue = deque()
queue.append((start, [start]))
visited = set()
visited.add(start)

found = False

while queue:
    (x, y), path = queue.popleft()

    if (x, y) == goal:
        print("Shortest Path:")
        print(path)
        print("Number of Steps:", len(path) - 1)
        found = True
        break

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if (0 <= nx < rows and
            0 <= ny < cols and
            maze[nx][ny] != '#' and
            (nx, ny) not in visited):

            visited.add((nx, ny))
            queue.append(((nx, ny), path + [(nx, ny)]))

if not found:
    print("No path found.")
