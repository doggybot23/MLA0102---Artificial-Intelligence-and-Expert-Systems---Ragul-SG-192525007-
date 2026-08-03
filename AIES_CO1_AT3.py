import math
import random
import heapq
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


def run_water_jug():
    print("\n" + "="*45)
    print("--- Water Jug (11L & 9L to 8L) ---")
    print("="*45)
    print("# Water Jug:")
    print("# (x, y) = (Amount in 11L jug, Amount in 9L jug)")
    print("# Target = 8L in either jug")
    print("="*45 + "\n")
    
    capA, capB, target = 11, 9, 8
    queue = deque([((0, 0), [])])
    visited = {(0, 0)}
    
    print(f"Jugs: {capA}L and {capB}L. Target: {target}L in either jug.\n")
    
    while queue:
        (a, b), steps = queue.popleft()
        
        if a == target or b == target:
            print(f"✨ Solution found in {len(steps)} steps!\n")
            print(f"{'Step':<6} | {'Action':<22} | {'11L Jug':<8} | {'9L Jug':<7}")
            print("-" * 53)
            print(f"{'0':<6} | {'Initial State':<22} | {'0L':<8} | {'0L':<7}")
            for i, (action, (st_a, st_b)) in enumerate(steps, 1):
                print(f"{i:<6} | {action:<22} | {str(st_a)+'L':<8} | {str(st_b)+'L':<7}")
            print("-" * 53)
            return
            
        transitions = [
            (capA, b, f"Fill 11L jug"),
            (a, capB, f"Fill 9L jug"),
            (0, b, f"Empty 11L jug"),
            (a, 0, f"Empty 9L jug"),
            (a - min(a, capB - b), b + min(a, capB - b), f"Pour 11L to 9L"),
            (a + min(b, capA - a), b - min(b, capA - a), f"Pour 9L to 11L")
        ]
        
        for na, nb, action in transitions:
            if (na, nb) not in visited:
                visited.add((na, nb))
                queue.append(((na, nb), steps + [(action, (na, nb))]))
                
    print("No solution possible.")


def run_connect_four():
    print("\n" + "="*45)
    print("--- Connect Four vs AI (Minimax & Alpha-Beta) ---")
    print("="*45)
    print("# Connect Four:")
    print("# X = Player")
    print("# O = AI")
    print("# . = Empty Slot")
    print("="*45 + "\n")
    
    ROWS, COLS = 6, 7
    EMPTY = 0
    PLAYER = 1
    AI = 2
    
    def create_board():
        return [[EMPTY] * COLS for _ in range(ROWS)]
        
    def drop_piece(board, row, col, piece):
        board[row][col] = piece
        
    def is_valid_location(board, col):
        return board[0][col] == EMPTY
        
    def get_next_open_row(board, col):
        for r in range(ROWS-1, -1, -1):
            if board[r][col] == EMPTY:
                return r
                
    def winning_move(board, piece):
        for c in range(COLS-3):
            for r in range(ROWS):
                if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece: return True
        for c in range(COLS):
            for r in range(ROWS-3):
                if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece: return True
        for c in range(COLS-3):
            for r in range(ROWS-3):
                if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece: return True
        for c in range(COLS-3):
            for r in range(3, ROWS):
                if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece: return True
        return False
        
    def evaluate_window(window, piece):
        score = 0
        opp_piece = PLAYER if piece == AI else AI
        if window.count(piece) == 4: score += 100
        elif window.count(piece) == 3 and window.count(EMPTY) == 1: score += 5
        elif window.count(piece) == 2 and window.count(EMPTY) == 2: score += 2
        if window.count(opp_piece) == 3 and window.count(EMPTY) == 1: score -= 4
        return score
        
    def score_position(board, piece):
        score = 0
        center_array = [board[r][COLS//2] for r in range(ROWS)]
        score += center_array.count(piece) * 3
        for r in range(ROWS):
            row_array = board[r]
            for c in range(COLS-3): score += evaluate_window(row_array[c:c+4], piece)
        for c in range(COLS):
            col_array = [board[r][c] for r in range(ROWS)]
            for r in range(ROWS-3): score += evaluate_window(col_array[r:r+4], piece)
        for r in range(ROWS-3):
            for c in range(COLS-3):
                window = [board[r+i][c+i] for i in range(4)]
                score += evaluate_window(window, piece)
        for r in range(ROWS-3):
            for c in range(COLS-3):
                window = [board[r+3-i][c+i] for i in range(4)]
                score += evaluate_window(window, piece)
        return score
        
    def is_terminal_node(board):
        return winning_move(board, PLAYER) or winning_move(board, AI) or len(get_valid_locations(board)) == 0
        
    def get_valid_locations(board):
        return [c for c in range(COLS) if is_valid_location(board, c)]
        
    def minimax(board, depth, alpha, beta, maximizingPlayer):
        valid_locations = get_valid_locations(board)
        is_terminal = is_terminal_node(board)
        if depth == 0 or is_terminal:
            if is_terminal:
                if winning_move(board, AI): return (None, 100000000000000)
                elif winning_move(board, PLAYER): return (None, -100000000000000)
                else: return (None, 0)
            else: return (None, score_position(board, AI))
            
        if maximizingPlayer:
            value = -math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = get_next_open_row(board, col)
                b_copy = [r[:] for r in board]
                drop_piece(b_copy, row, col, AI)
                new_score = minimax(b_copy, depth-1, alpha, beta, False)[1]
                if new_score > value:
                    value, column = new_score, col
                alpha = max(alpha, value)
                if alpha >= beta: break
            return column, value
        else:
            value = math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = get_next_open_row(board, col)
                b_copy = [r[:] for r in board]
                drop_piece(b_copy, row, col, PLAYER)
                new_score = minimax(b_copy, depth-1, alpha, beta, True)[1]
                if new_score < value:
                    value, column = new_score, col
                beta = min(beta, value)
                if alpha >= beta: break
            return column, value

    def print_board(board):
        symbols = {EMPTY: '.', PLAYER: 'X', AI: 'O'}
        print("")
        for r in board:
            print("  " + " ".join(symbols[x] for x in r))
        print("  " + " ".join(str(i) for i in range(COLS)) + "\n")

    board = create_board()
    game_over = False
    turn = 0 
    
    print("You are 'X', AI is 'O'. Enter column number (0-6) to drop your piece.")
    print_board(board)
    
    while not game_over:
        if turn == 0:
            user_input = input("Player (X) Selection (0-6) or 'q' to quit: ")
            if user_input.lower() == 'q':
                print("Exiting Connect Four.")
                break
            try:
                col = int(user_input)
            except ValueError:
                print("Invalid input! Please enter a number 0-6.")
                continue
                
            if 0 <= col < COLS and is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, PLAYER)
                if winning_move(board, PLAYER):
                    print_board(board)
                    print("🎉 CONGRATULATIONS! YOU WIN!")
                    game_over = True
                turn = (turn + 1) % 2
                print_board(board)
            else:
                print("Invalid column or column is full. Try again.")
        else:
            print("AI (O) is thinking...")
            col, minimax_score = minimax(board, 5, -math.inf, math.inf, True)
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, AI)
                if winning_move(board, AI):
                    print_board(board)
                    print("💻 AI WINS! Better luck next time.")
                    game_over = True
                turn = (turn + 1) % 2
                print_board(board)
                
            if len(get_valid_locations(board)) == 0 and not game_over:
                print("IT'S A DRAW!")
                game_over = True


def run_8_puzzle():
    print("\n" + "="*30)
    print("--- 8-Puzzle (A* Algorithm) ---")
    print("="*30)
    print("# 8-Puzzle:")
    print("# 1-8 = Numbered Tiles")
    print("# 0   = Empty Space")
    print("="*30 + "\n")
    
    initial_state = (2, 8, 3, 1, 6, 4, 7, 0, 5)
    goal_state = (1, 2, 3, 8, 0, 4, 7, 6, 5)
    
    def manhattan(state):
        dist = 0
        for i in range(9):
            val = state[i]
            if val != 0:
                target_idx = goal_state.index(val)
                tr, tc = divmod(target_idx, 3)
                cr, cc = divmod(i, 3)
                dist += abs(tr - cr) + abs(tc - cc)
        return dist
        
    def print_state(state, prefix="  "):
        print(f"{prefix}{state[0]} {state[1]} {state[2]}")
        print(f"{prefix}{state[3]} {state[4]} {state[5]}")
        print(f"{prefix}{state[6]} {state[7]} {state[8]}\n")
        
    print("Solving with A* search... Please wait.\n")

    pq = []
    # Store path as a list of tuples: (move_description, state)
    heapq.heappush(pq, (manhattan(initial_state), 0, 0, initial_state, [("Initial State", initial_state)]))
    visited = set()
    counter = 1 
    
    move_names = {
        (-1, 0): "Moved Empty Space UP",
        (1, 0):  "Moved Empty Space DOWN",
        (0, -1): "Moved Empty Space LEFT",
        (0, 1):  "Moved Empty Space RIGHT"
    }
    
    while pq:
        f, _, g, current, path = heapq.heappop(pq)
        
        if current == goal_state:
            print(f"✨ Goal reached in {g} moves!\n")
            print("--- Step-by-Step Path ---")
            for idx, (move_str, s) in enumerate(path):
                if idx == 0:
                    print(f"Start -> {move_str}:")
                else:
                    print(f"Step {idx} -> {move_str}:")
                print_state(s)
            return
            
        if current in visited:
            continue
        visited.add(current)
        
        zero_idx = current.index(0)
        zr, zc = divmod(zero_idx, 3)
        
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = zr + dr, zc + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                n_idx = nr * 3 + nc
                new_state = list(current)
                new_state[zero_idx], new_state[n_idx] = new_state[n_idx], new_state[zero_idx]
                new_state = tuple(new_state)
                
                if new_state not in visited:
                    new_g = g + 1
                    new_f = new_g + manhattan(new_state)
                    move_str = move_names[(dr, dc)]
                    heapq.heappush(pq, (new_f, counter, new_g, new_state, path + [(move_str, new_state)]))
                    counter += 1
                    
    print("No solution found.")


def main():
    while True:
        print("\n" + "="*45)
        print("          AI LAB - 5 PROGRAMS BUNDLE")
        print("="*45)
        print(" 1. Maze Escape (BFS)")
        print(" 2. 12-Queens (Backtracking)")
        print(" 3. Water Jug (11L/9L to 8L via BFS)")
        print(" 4. Connect Four vs AI (Minimax + Alpha-Beta)")
        print(" 5. 8-Puzzle (A* Algorithm)")
        print(" 6. Exit")
        print("="*45)
        
        choice = input("Select an option (1-6): ").strip()
        
        if choice == '1':
            run_maze_escape()
        elif choice == '2':
            run_12_queens()
        elif choice == '3':
            run_water_jug()
        elif choice == '4':
            run_connect_four()
        elif choice == '5':
            run_8_puzzle()
        elif choice == '6':
            print("\nExiting AI Lab Bundle. Goodbye!\n")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
