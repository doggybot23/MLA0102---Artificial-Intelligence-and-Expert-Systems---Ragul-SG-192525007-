import math
import random

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

if __name__ == "__main__":
    run_connect_four()
