grid = [
    ['S', '.', '.', '.', '.', '.', '.'],
    ['.', '#', '.', '.', '#', '.', '.'],
    ['.', '.', '.', '#', '.', '.', '#'],
    ['.', '#', '.', '.', '.', '#', '.'],
    ['.', '.', '#', '.', '.', '.', 'G']
]

rows = len(grid)
cols = len(grid[0])

visited = [[False] * cols for _ in range(rows)]

moves = [(1,0),(-1,0),(0,1),(0,-1)]

def dfs(x, y):

    if x < 0 or y < 0 or x >= rows or y >= cols:
        return False

    if grid[x][y] == '#' or visited[x][y]:
        return False

    visited[x][y] = True
    print((x, y), end=" ")

    if grid[x][y] == 'G':
        print("\nGoal Reached")
        return True

    for dx, dy in moves:
        if dfs(x + dx, y + dy):
            return True

    return False

dfs(0, 0)
