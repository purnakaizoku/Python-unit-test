import unittest
from unittest import mock
import ChessRules
from ChessBoard import ChessBoard

class CheckIsCheckmate(unittest.TestCase):
    """Class to unit check the IsCheckmate method of ChessRules.py module"""

    @mock.patch('ChessRules.ChessRules.GetListOfValidMoves')
    def test_call_count(self, mockGetListOfValidMoves):
        """Unit test for ChessRules method: IsCheckmate"""
        # Creating objects of Chessboard and ChessRules class
        cb = ChessBoard(0)  # Create a chess board object with the initial position
        chess_rules_obj = ChessRules.ChessRules()
        chess_rules_obj.IsCheckmate(cb.GetState(), "black")

        # Create expected_arg_calls list which is supposed to be called with GetListOfValidMoves for initial position
        # IsCheckmate calls GetListOfValidMoves with arguments: board, color (who is to play?) and co-ordinates of a square with a piece on it
        expected_arg_calls = []
        for row in range(0, 2):
            for col in range(0, 8):
                expected_arg_calls.append(mock.call(cb.GetState(), 'black', (row, col)))

        # check the number of times your mocked method was called
        self.assertEqual(mockGetListOfValidMoves.call_count, 16)

if __name__ == "__main__":
    unittest.main()
