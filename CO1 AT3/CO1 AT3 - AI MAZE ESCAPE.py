from collections import deque

def run_maze_escape():
    print("\n" + "="*30)
    print("--- Maze Escape (BFS) ---")
    print("="*30)
    print("# Maze:")
    print("# S = Start")
    print("# G = Goal")
    print("# # = Wall")
    print("# . = Free Path")
    print("="*30 + "\n")
    
    # 0 represents path, 1 represents wall
    maze = [
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 0],
        [0, 0, 0, 1, 0, 0],
        [1, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0]
    ]
    rows, cols = len(maze), len(maze[0])
    start = (0, 0)
    goal = (4, 5)
    
    print(f"Maze Grid ({rows}x{cols}):")
    for r in range(rows):
        row_str = []
        for c in range(cols):
            if (r, c) == start:
                row_str.append('S')
            elif (r, c) == goal:
                row_str.append('G')
            elif maze[r][c] == 1:
                row_str.append('#')
            else:
                row_str.append('.')
        print("  " + " ".join(row_str))
    print(f"\nStart: {start}, Goal: {goal}\n")

    queue = deque([(start, [start])])
    visited = {start}
    
    while queue:
        (r, c), path = queue.popleft()
        
        if (r, c) == goal:
            print(f"Success! Path found in {len(path)-1} steps:")
            print(" -> ".join([f"({pr},{pc})" for pr, pc in path]))
            return
            
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0:
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append(((nr, nc), path + [(nr, nc)]))
                    
    print("No path found.")

if __name__ == "__main__":
    run_maze_escape()
