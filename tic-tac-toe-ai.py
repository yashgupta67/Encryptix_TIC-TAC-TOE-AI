class TicTacToe:
    def __init__(self):
        self.board = [None] * 9

    def display_board(self):
        for i in range(0, 9, 3):
            row = [' ' if x is None else x for x in self.board[i:i+3]]
            print('|'.join(row))
            if i < 6:
                print('-----')

    def is_winner(self, player):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        return any(all(self.board[i] == player for i in combo) for combo in win_combinations)

    def available_moves(self):
        return [i for i in range(9) if self.board[i] is None]

    def is_draw(self):
        return all(spot is not None for spot in self.board) and not self.is_winner("X") and not self.is_winner("O")

    def minimax(self, depth, is_maximizing):
        if self.is_winner("X"):
            return -1
        if self.is_winner("O"):
            return 1
        if self.is_draw():
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for move in self.available_moves():
                self.board[move] = "O"
                score = self.minimax(depth + 1, False)
                self.board[move] = None
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for move in self.available_moves():
                self.board[move] = "X"
                score = self.minimax(depth + 1, True)
                self.board[move] = None
                best_score = min(score, best_score)
            return best_score

    def best_move(self):
        best_score = -float('inf')
        move = None
        for i in self.available_moves():
            self.board[i] = "O"
            score = self.minimax(0, False)
            self.board[i] = None
            if score > best_score:
                best_score = score
                move = i
        return move

    def make_move(self, position, player):
        if self.board[position] is None:
            self.board[position] = player
            return True
        return False

    def play_game(self):
        human = "X"
        ai = "O"
        while True:
            self.display_board()
            try:
                move = int(input("Enter your move (0-8): "))
                if move not in self.available_moves():
                    print("Invalid move. Try again.")
                    continue
            except ValueError:
                print("Invalid input. Enter a number from 0 to 8.")
                continue

            self.make_move(move, human)
            if self.is_winner(human):
                self.display_board()
                print("You win!")
                break
            if self.is_draw():
                self.display_board()
                print("It's a draw!")
                break

            ai_move = self.best_move()
            self.make_move(ai_move, ai)
            if self.is_winner(ai):
                self.display_board()
                print("AI wins!")
                break
            if self.is_draw():
                self.display_board()
                print("It's a draw!")
                break

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
