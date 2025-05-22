import math

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def display_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def make_move(self, row, col, player):
        if self.board[row][col] == ' ':
            self.board[row][col] = player
            return True
        return False

    def undo_move(self, row, col):
        self.board[row][col] = ' '

    def check_winner(self):
        b = self.board
        lines = [
            # Rows
            b[0], b[1], b[2],
            # Columns
            [b[0][0], b[1][0], b[2][0]],
            [b[0][1], b[1][1], b[2][1]],
            [b[0][2], b[1][2], b[2][2]],
            # Diagonals
            [b[0][0], b[1][1], b[2][2]],
            [b[0][2], b[1][1], b[2][0]],
        ]
        for line in lines:
            if line[0] == line[1] == line[2] != ' ':
                return line[0]
        return None

    def is_draw(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def minimax(self, depth, alpha, beta, is_maximizing):
        winner = self.check_winner()
        if winner == 'O':
            return 1
        elif winner == 'X':
            return -1
        elif self.is_draw():
            return 0

        if is_maximizing:
            max_eval = -math.inf
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.make_move(i, j, 'O')
                        eval = self.minimax(depth + 1, alpha, beta, False)
                        self.undo_move(i, j)
                        max_eval = max(max_eval, eval)
                        alpha = max(alpha, eval)
                        if beta <= alpha:
                            break  # Beta cut-off
            return max_eval
        else:
            min_eval = math.inf
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.make_move(i, j, 'X')
                        eval = self.minimax(depth + 1, alpha, beta, True)
                        self.undo_move(i, j)
                        min_eval = min(min_eval, eval)
                        beta = min(beta, eval)
                        if beta <= alpha:
                            break  # Alpha cut-off
            return min_eval

    def best_move(self):
        best_score = -math.inf
        move = None
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.make_move(i, j, 'O')
                    score = self.minimax(0, -math.inf, math.inf, False)
                    self.undo_move(i, j)
                    if score > best_score:
                        best_score = score
                        move = (i, j)
        return move

    def play(self):
        current_player = 'X'  # Human starts
        while True:
            self.display_board()

            if current_player == 'X':
                try:
                    row = int(input("Enter row (0-2): "))
                    col = int(input("Enter column (0-2): "))
                except ValueError:
                    print("Invalid input. Try again.")
                    continue
                if not (0 <= row < 3 and 0 <= col < 3):
                    print("Out of bounds. Try again.")
                    continue
                if not self.make_move(row, col, 'X'):
                    print("Cell taken. Try again.")
                    continue
            else:
                print("AI is making a move...")
                row, col = self.best_move()
                self.make_move(row, col, 'O')

            winner = self.check_winner()
            if winner:
                self.display_board()
                print(f"Player {winner} wins!")
                break
            elif self.is_draw():
                self.display_board()
                print("It's a draw!")
                break

            current_player = 'O' if current_player == 'X' else 'X'
game = TicTacToe()
game.play()
