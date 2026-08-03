def run_12_queens():
    print("\n" + "="*30)
    print("--- 12-Queens (Backtracking) ---")
    print("="*30)
    print("# 12-Queens:")
    print("# Q = Queen")
    print("# . = Empty Square")
    print("="*30 + "\n")
    
    N = 12
    board = [[0] * N for _ in range(N)]
    
    def is_safe(r, c):
        for i in range(c):
            if board[r][i] == 1: return False
        for i, j in zip(range(r, -1, -1), range(c, -1, -1)):
            if board[i][j] == 1: return False
        for i, j in zip(range(r, N, 1), range(c, -1, -1)):
            if board[i][j] == 1: return False
        return True
        
    def solve(col):
        if col >= N: return True
        for i in range(N):
            if is_safe(i, col):
                board[i][col] = 1
                if solve(col + 1):
                    return True
                board[i][col] = 0 # Backtrack
        return False
        
    print("Searching for a solution...")
    if solve(0):
        print(f"\nSolution for {N}-Queens:")
        for row in board:
            print("  " + " ".join("Q" if x == 1 else "." for x in row))
    else:
        print("No solution exists.")

if __name__ == "__main__":
    run_12_queens()
