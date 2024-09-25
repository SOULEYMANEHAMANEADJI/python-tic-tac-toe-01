import unittest
import numpy as np
from tic_tac_toe import empty_board, random_place, row_winner, column_winner, diagonal_winner, evaluate_game


class TestTicTacToe(unittest.TestCase):

    def test_empty_board(self):
        board = empty_board()
        # Test if the board is created with all zeros
        self.assertTrue(np.array_equal(board, np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])))

    def test_random_place(self):
        board = empty_board()
        board = random_place(board, 1)
        # Test if a valid move (i.e., player 1) was made on an empty board
        self.assertEqual(np.count_nonzero(board == 1), 1)

    def test_row_winner(self):
        board = np.array([[1, 1, 1], [0, 0, 0], [0, 0, 0]])
        # Test if player 1 wins on a row
        self.assertTrue(row_winner(board, 1))
        self.assertFalse(row_winner(board, 2))

    def test_column_winner(self):
        board = np.array([[2, 0, 0], [2, 0, 0], [2, 0, 0]])
        # Test if player 2 wins on a column
        self.assertTrue(column_winner(board, 2))
        self.assertFalse(column_winner(board, 1))

    def test_diagonal_winner(self):
        board = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        # Test if player 1 wins on the main diagonal
        self.assertTrue(diagonal_winner(board, 1))
        self.assertFalse(diagonal_winner(board, 2))

        board = np.array([[0, 0, 2], [0, 2, 0], [2, 0, 0]])
        # Test if player 2 wins on the anti-diagonal
        self.assertTrue(diagonal_winner(board, 2))
        self.assertFalse(diagonal_winner(board, 1))

    def test_evaluate_game(self):
        # Test case where Player 1 wins on a row
        board = np.array([[1, 1, 1], [0, 0, 0], [0, 0, 0]])
        self.assertEqual(evaluate_game(board), 1)

        # Test case where Player 2 wins on a column
        board = np.array([[2, 0, 0], [2, 0, 0], [2, 0, 0]])
        self.assertEqual(evaluate_game(board), 2)

        # Test case where it's a tie
        board = np.array([[1, 2, 1], [1, 2, 2], [2, 1, 1]])
        self.assertEqual(evaluate_game(board), -1)

        # Test case where the game is not finished yet
        board = np.array([[1, 0, 1], [1, 2, 2], [0, 1, 0]])
        self.assertEqual(evaluate_game(board), 0)


if __name__ == '__main__':
    unittest.main()