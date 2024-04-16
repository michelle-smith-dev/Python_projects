import unittest
# import TicTacToe
from TicTacToe import TicTacToe

class MyTestCase(unittest.TestCase):

    # def test_run_method(self):


    def test_update_board(self):
        update = TicTacToe()
        update.update_board(0, 1, "X")
        assert update.display_board()[0][1] == "X"
# **Update this function to require integer and string types for vals 1 & 2 and player
# Test if passing invalid parameters in function, the function throws an error
# Test board is upated with values and player X or O
# Test moves counter is updated

#     def test_convert_to_ij(self):
#         self.assertEqual(TicTacToe.convert_to_ij(8), (2, 2))
#         self.assertEqual(TicTacToe.convert_to_ij(0), (0, 0))
#         self.assertEqual(TicTacToe.convert_to_ij(4), (1, 1))
#
#     def test_cpu_move(self):
#
# # test random number returns valid index numbers, i and j
# # test a valid number found on the board is chosen
# # test if random number is not valid, the while loop will run until a valid number is chosen
#
#
#     def test_win_condition(self):
#
# # Test if no player parameter is provided, the function will return False
# # Test if one of the conditions is met, the function returns True
# # Test with a board that is mostly full of X's and O's but there is no tic tac toe
#
#     def test_get_user_input(self):
# 
# # Test user input only accepts integer value
# # Test if user input is out of range, it will continue to prompt user for correct range of input
# # Test if input is converted properly to index values, i, j
# # Test i, j is only returned if the space is available on the board, i.e. is a valid space


if __name__ == '__main__':
    unittest.main()
