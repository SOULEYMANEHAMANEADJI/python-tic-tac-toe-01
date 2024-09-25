import numpy as np
import random
from time import sleep

# Creating an empty Tic-Tac-Toe Board
def empty_board():
    return np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

# Check for empty places on the Tic-Tac-Toe Board
def empty_places(board):
    return [(i, j) for i in range(len(board)) for j in range(len(board)) if board[i, j] == 0]

# Select a random place for the player on the Tic-Tac-Toe Board
def random_place(board, player):
    available_places = empty_places(board)
    current_location = random.choice(available_places)
    board[current_location] = player
    return board

# Check the horizontal rows for a winner
def row_winner(board, player):
    return np.any(np.all(board == player, axis=1))

# Check the vertical columns for a winner
def column_winner(board, player):
    return np.any(np.all(board == player, axis=0))

# Check the diagonal rows for a winner
def diagonal_winner(board, player):
    return np.all(np.diag(board) == player) or np.all(np.diag(np.fliplr(board)) == player)

# Evaluates whether there is a winner or a tie
def evaluate_game(board):
    winner = 0
    for player in [1, 2]:
        if row_winner(board, player) or column_winner(board, player) or diagonal_winner(board, player):
            winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1  # It's a tie
    return winner

# Display the Tic-Tac-Toe board in a more readable format
def display_board(board):
    symbols = {0: " ", 1: "X", 2: "O"}
    display = np.vectorize(symbols.get)(board)
    print(display)

# Main function to run/start the game
def tic_tac_toe():
    board = empty_board()
    winner = 0
    counter = 1
    sleep(1)  # Shorter sleep to make the game more interactive
    while winner == 0:
        for player in [1, 2]:
            board = random_place(board, player)
            print(f"Board after {counter} move:")
            display_board(board)
            sleep(1)
            counter += 1
            winner = evaluate_game(board)
            if winner != 0:
                break
    return winner

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Run the game and print the winner
    print("Winner is player: " + str(tic_tac_toe()))
