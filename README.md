# Encryptix_TIC-TAC-TOE-AI
A Tic-Tac-Toe game where an AI plays against a human player. The AI uses the Minimax algorithm to make it unbeatable

This project showcases a classic game of Tic-Tac-Toe with an AI opponent that utilizes the Minimax algorithm, a widely used recursive algorithm in decision-making and game theory. The AI, which plays as "O," employs the Minimax algorithm to carefully evaluate all possible moves and counter-moves to determine the best possible outcome against a perfect opponent. The AI aims to win the game or force a draw by considering future potential moves and their associated outcomes. The game is presented through a console-based interface, allowing the human player, represented by "X," to move on a 3x3 grid. This project is an excellent example of how the Minimax algorithm can be applied to create a competitive and intelligent game opponent, providing an insightful demonstration of search algorithms in turn-based games.


## Key Components
1. Game Representation: A way to represent the Tic-Tac-Toe board and track moves.
2. Minimax Algorithm: The core algorithm that evaluates the optimal move.
3. Alpha-Beta Pruning: An optimization of Minimax that reduces the number of nodes evaluated.


## How it Works
AI vs. Human: The AI uses the Minimax algorithm to decide its moves, making it unbeatable as it always aims to minimize the potential loss.
Interaction: The human player enters moves by typing numbers from 0 to 8, corresponding to board positions.
Board Display: The board is displayed in the console after each move.
