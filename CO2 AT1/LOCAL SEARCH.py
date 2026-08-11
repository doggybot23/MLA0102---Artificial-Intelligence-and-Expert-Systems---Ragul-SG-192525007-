# Online Search Agent (Dynamic Path Finding)

grid = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],   # 1 = Obstacle
    [0, 0, 0, 0],
    [0, 0, 1, 0]
]

start = (0, 0)
goal = (3, 3)

moves = [(0,1), (1,0), (0,-1), (-1,0)]

def online_search(start, goal):
    current = start
    path = [current]

    while current != goal:
        x, y = current
        found = False

        for dx, dy in moves:
            nx, ny = x + dx, y + dy

            if 0 <= nx < 4 and 0 <= ny < 4:
                if grid[nx][ny] == 0 and (nx, ny) not in path:
                    current = (nx, ny)
                    path.append(current)
                    found = True
                    break

        if not found:
            print("No Path Exists")
            return

    print("Path Found:")
    print(path)

online_search(start, goal)
