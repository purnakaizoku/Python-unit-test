import unittest
from unittest import mock
from ChessBoard import ChessBoard
import ChessRules

class CheckIsCheckmate(unittest.TestCase):
    """Class to unit check the IsCheckmate method of ChessRules.py module"""

    @mock.patch('ChessRules.GetListOfValidMoves')
    def test_called_with_args(self, mockGetListOfValidMoves):
        """Unit test for ChessRules method: IsCheckmate"""
        # Creating objects of Chessboard and ChessRules class
        cb = ChessBoard(0)  # Create a chess board object with the initial position
        chess_rules_obj = ChessRules.ChessRules()

        # Calling IsCheckmate function with each piece for initial position and "black" color
        chess_rules_obj.IsCheckmate(cb.GetState(), "black")

        # Create expected_arg_calls list which is supposed to be called with GetListOfValidMoves for initial position
        # IsCheckmate calls GetListOfValidMoves with arguments: board, color (who is to play?) and co-ordinates of a square with a piece on it
        expected_arg_calls = [mock.call(cb.GetState(), 'black', (row, col)) for row in range(0, 2) for col in range(0, 8)]

        # Assert that method was called at least once with some argument
        mockGetListOfValidMoves.assert_any_ca
