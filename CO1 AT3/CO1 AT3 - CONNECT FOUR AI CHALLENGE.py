# Connect Four AI Challenge
# Human vs AI using Minimax with Alpha-Beta Pruning

import math
import random

ROW_COUNT = 6
COLUMN_COUNT = 7

EMPTY = 0
PLAYER = 1
AI = 2

def create_board():
    return [[0 for _ in range(COLUMN_COUNT)] for _ in range(ROW_COUNT)]

def print_board(board):
    print()
    for row in board:
        print(" ".join(str(x) for x in row))
    print("0 1 2 3 4 5 6\n")

def is_valid_location(board, col):
    return board[0][col] == EMPTY

def get_next_open_row(board, col):
    for r in range(ROW_COUNT - 1, -1, -1):
        if board[r][col] == EMPTY:
            return r

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def winning_move(board, piece):
    # Horizontal
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT - 3):
            if all(board[r][c+i] == piece for i in range(4)):
                return True

    # Vertical
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if all(board[r+i][c] == piece for i in range(4)):
                return True

    # Positive diagonal
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            if all(board[r+i][c+i] == piece for i in range(4)):
                return True

    # Negative diagonal
    for r in range(3, ROW_COUNT):
        for c in range(COLUMN_COUNT - 3):
            if all(board[r-i][c+i] == piece for i in range(4)):
                return True

    return False

def get_valid_locations(board):
    return [c for c in range(COLUMN_COUNT) if is_valid_location(board, c)]

def evaluate_window(window, piece):
    score = 0
    opp = PLAYER if piece == AI else AI

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(EMPTY) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(EMPTY) == 2:
        score += 2

    if window.count(opp) == 3 and window.count(EMPTY) == 1:
        score -= 4

    return score

def score_position(board, piece):
    score = 0

    # Center column preference
    center = [board[r][COLUMN_COUNT//2] for r in range(ROW_COUNT)]
    score += center.count(piece) * 3

    # Horizontal
    for r in range(ROW_COUNT):
        row = board[r]
        for c in range(COLUMN_COUNT - 3):
            score += evaluate_window(row[c:c+4], piece)

    # Vertical
    for c in range(COLUMN_COUNT):
        col = [board[r][c] for r in range(ROW_COUNT)]
        for r in range(ROW_COUNT - 3):
            score += evaluate_window(col[r:r+4], piece)

    # Positive diagonal
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            window = [board[r+i][c+i] for i in range(4)]
            score += evaluate_window(window, piece)

    # Negative diagonal
    for r in range(3, ROW_COUNT):
        for c in range(COLUMN_COUNT - 3):
            window = [board[r-i][c+i] for i in range(4)]
            score += evaluate_window(window, piece)

    return score

def minimax(board, depth, alpha, beta, maximizing):
    valid = get_valid_locations(board)

    if winning_move(board, AI):
        return (None, 100000)
    if winning_move(board, PLAYER):
        return (None, -100000)
    if depth == 0 or len(valid) == 0:
        return (None, score_position(board, AI))

    if maximizing:
        value = -math.inf
        column = random.choice(valid)

        for col in valid:
            row = get_next_open_row(board, col)
            temp = [r[:] for r in board]
            drop_piece(temp, row, col, AI)
            new_score = minimax(temp, depth-1, alpha, beta, False)[1]

            if new_score > value:
                value = new_score
                column = col

            alpha = max(alpha, value)
            if alpha >= beta:
                break

        return column, value

    else:
        value = math.inf
        column = random.choice(valid)

        for col in valid:
            row = get_next_open_row(board, col)
            temp = [r[:] for r in board]
            drop_piece(temp, row, col, PLAYER)
            new_score = minimax(temp, depth-1, alpha, beta, True)[1]

            if new_score < value:
                value = new_score
                column = col

            beta = min(beta, value)
            if alpha >= beta:
                break

        return column, value

# -------------------- Main --------------------

board = create_board()
game_over = False
turn = PLAYER

print("Connect Four")
print("Player = 1 | AI = 2")
print_board(board)

while not game_over:

    if turn == PLAYER:
        col = int(input("Enter column (0-6): "))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, PLAYER)

            if winning_move(board, PLAYER):
                print_board(board)
                print("You Win!")
                break

            turn = AI

    else:
        print("AI is thinking...")
        col, _ = minimax(board, 4, -math.inf, math.inf, True)

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, AI)

            if winning_move(board, AI):
                print_board(board)
                print("AI Wins!")
                break

            turn = PLAYER

    print_board(board)

    if len(get_valid_locations(board)) == 0:
        print("Game Draw!")
        break
