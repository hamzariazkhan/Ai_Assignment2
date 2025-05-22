import time

# Tic-Tac-Toe Game Core
def print_board(board):
    for row in board:
        print("|".join(row))
    print()

def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] != '_' and all(board[i][j] == board[i][0] for j in range(3)):
            return board[i][0]
        if board[0][i] != '_' and all(board[j][i] == board[0][i] for j in range(3)):
            return board[0][i]
    # Check diagonals
    if board[0][0] != '_' and all(board[i][i] == board[0][0] for i in range(3)):
        return board[0][0]
    if board[0][2] != '_' and all(board[i][2-i] == board[0][2] for i in range(3)):
        return board[0][2]
    return None

def is_full(board):
    return all(cell != '_' for row in board for cell in row)

# Standard Minimax Algorithm
def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == 'X': return 1
    if winner == 'O': return -1
    if is_full(board): return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'X'
                    score = minimax(board, False)
                    board[i][j] = '_'
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'O'
                    score = minimax(board, True)
                    board[i][j] = '_'
                    best_score = min(score, best_score)
        return best_score

# Minimax with Alpha-Beta Pruning
def minimax_ab(board, depth, alpha, beta, is_maximizing):
    winner = check_winner(board)
    if winner == 'X': return 1
    if winner == 'O': return -1
    if is_full(board): return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'X'
                    score = minimax_ab(board, depth + 1, alpha, beta, False)
                    board[i][j] = '_'
                    best_score = max(score, best_score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'O'
                    score = minimax_ab(board, depth + 1, alpha, beta, True)
                    board[i][j] = '_'
                    best_score = min(score, best_score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
        return best_score

# Best move functions
def best_move_minimax(board):
    best_score = float('-inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = 'X'
                score = minimax(board, False)
                board[i][j] = '_'
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def best_move_ab(board):
    best_score = float('-inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = 'X'
                score = minimax_ab(board, 0, float('-inf'), float('inf'), False)
                board[i][j] = '_'
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Performance Comparison
def compare_performance():
    board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

    start = time.time()
    best_move_minimax(board)
    end = time.time()
    print(f"Minimax Time: {end - start:.6f} seconds")

    start = time.time()
    best_move_ab(board)
    end = time.time()
    print(f"Alpha-Beta Time: {end - start:.6f} seconds")

if __name__ == "__main__":
    compare_performance()
