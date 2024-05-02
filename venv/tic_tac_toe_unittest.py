import unittest
from TicTacToe import TicTacToe
from unittest.mock import patch, MagicMock

class MyTestCase(unittest.TestCase):

#     # def test_run_method(self):
#
#
#     def test_update_board(self):
#         update = TicTacToe()
#
#         # Test updating the board is actually updated with an X or an O
#         update.update_board(0, 1, "X")
#         assert update.display_board()[0][1] == "X"
#         update.update_board(2, 1, "O")
#         assert update.display_board()[0][1] == "X"
#
#         # Test when update board is ran, the moves variable adds +1 for each update_board move
#         assert update.moves == 2
#
#         # Test invalid index parameters raises an exception
#         with self.assertRaises(IndexError):
#             update.update_board(3, 1, "X")
#         with self.assertRaises(IndexError):
#             update.update_board(2, 4, "O")
#         with self.assertRaises(TypeError):
#             update.update_board("hello", 1, "O")
#
#         # Test filling the board with O's
#         m, n = 0, 0
#         for ele_m in range(3):
#             for ele_n in range(3):
#                 # print(ele_m, ele_n)
#                 update.update_board(m, n, "O")
#                 assert update.board[m][n] == 'O'
#                 if ele_m == 2 and ele_n == 2:
#                     break
#                 n += 1
#             m += 1
#             n = 0
#
#     def test_convert_to_ij(self):
#
#         # Test function can convert integers successfully
#         self.assertEqual(TicTacToe.convert_to_ij(8), (2, 2))
#         self.assertEqual(TicTacToe.convert_to_ij(0), (0, 0))
#         self.assertEqual(TicTacToe.convert_to_ij(4), (1, 1))
#         self.assertEqual(TicTacToe.convert_to_ij(-1), (-1, 2))
#         self.assertEqual(TicTacToe.convert_to_ij(1022), (340, 2))
#         self.assertEqual(TicTacToe.convert_to_ij(1.22), (0.0, 1.22))
#
#         # Test function raises an error when integer is not passed
#         with self.assertRaises(TypeError):
#             TicTacToe.convert_to_ij("Hello")
#
#     def test_cpu_move_blank_board(self):
#         ttt = TicTacToe()
#
#         # Test if i, j returned in cpu_move function is in valid range
#         for element in ttt.cpu_move():
#             print("cpu_move value:", element)
#             assert element <= 2
#
#         # Loop the cpu_move until all values on the board have been chosen
#         while ttt.moves < 9:
#             cpu_input = ttt.cpu_move()
#             i, j = cpu_input  # Return CPU value as coordinates on the board to use index values to update board
#             ttt.update_board(i, j, "X")
#             if ttt.moves >= 9:
#                 ttt.display_board()
#
#         assert ttt.moves == 9
#
#         # Loop through blank cpu_move board 100 times -- iteratively
#         loops = 0
#         while loops is not 100:
#             ttt = TicTacToe()
#
#             while ttt.moves < 9:
#                 cpu_input = ttt.cpu_move()
#                 i, j = cpu_input  # Return CPU value as coordinates on the board to use index values to update board
#                 ttt.update_board(i, j, "X")
#                 if ttt.moves >= 9:
#                     ttt.display_board()
#                     assert ttt.moves == 9
#
#             loops += 1
#
#         assert loops == 100
#
#
#     # # Loop through cpu_move function a hundred times with an empty board -- recursively
#     # def test_cpu_move_recursively(self, loops=100):
#     #     ttt = TicTacToe()
#     #     cpu_move = ttt.cpu_move()
#     #
#     #     while ttt.moves < 9:
#     #         cpu_input = ttt.cpu_move()
#     #         i, j = cpu_input  # Return CPU value as coordinates on the board to use index values to update board
#     #         ttt.update_board(i, j, "X")
#     #         if ttt.moves >= 9:
#     #             assert ttt.moves == 9
#     #             if loops is not 0:
#     #                 return self.test_cpu_move_recursively(loops-1)
#     #             else:
#     #                 assert loops == 0
#     #                 return False
#
#
    # Start with board filled with all 'O' player moves and reduce by 1 'O' player to verify cpu_move can fill remaining board
    # def test_cpu_move_filled_board(self):
    #     ttt = TicTacToe()
    #
    #     loops = 10
    #     while loops:
    #         ttt = TicTacToe()
    #
    #         for i in range(loops-1):
    #             user_input = ttt.cpu_move()
    #             k, m = user_input
    #             ttt.update_board(k, m, "O")
    #         assert ttt.moves == loops-1
    #
    #         while ttt.moves < 9:
    #             cpu_input = ttt.cpu_move()
    #             i, j = cpu_input  # Return CPU value as coordinates on the board to use index values to update board
    #             ttt.update_board(i, j, "X")
    #             if ttt.moves >= 9:
    #                 ttt.display_board()
    #                 assert ttt.moves == 9
    #         loops -= 1


    def test_win_condition(self):
        ttt = TicTacToe()

        # Test the board with winning condition for player 'X'
        ttt.update_board(0, 1, "X")
        ttt.update_board(0, 0, "X")
        ttt.update_board(0, 2, "X")
        check_board = ttt.win_condition("X")
        assert check_board == True

        # Test the board with 2 moves for X and 1 move for O
        ttt = TicTacToe()
        ttt.update_board(0, 1, "X")
        ttt.update_board(0, 0, "X")
        ttt.update_board(0, 2, "O")
        check_board = ttt.win_condition("X")
        assert check_board == False

        # Test the board various moves from both players, no win
        ttt = TicTacToe()
        ttt.update_board(0, 0, "X")
        ttt.update_board(0, 1, "X")
        ttt.update_board(0, 2, "O")
        ttt.update_board(1, 1, "O")
        ttt.update_board(2, 2, "O")
        ttt.update_board(1, 2, "X")
        # Assert no win for Player X
        check_board = ttt.win_condition("X")
        assert check_board == False

        # Assert no win for Player O
        check_board = ttt.win_condition("O")
        assert check_board == False

        # Test the win condition for player who does not have the win
        ttt = TicTacToe()
        ttt.update_board(0, 0, "X")
        ttt.update_board(0, 1, "X")
        ttt.update_board(0, 2, "O")
        ttt.update_board(1, 1, "X")
        ttt.update_board(2, 2, "O")
        ttt.update_board(1, 0, "X")
        ttt.update_board(1, 2, "O")

        check_board = ttt.win_condition("X")
        assert check_board == False

        # Test if no player parameter is specified, an error occurs
        with self.assertRaises(TypeError):
            check_condition = ttt.win_condition()

        # Check win occurs while looping through playing the board
        ttt = TicTacToe()
        loops = 10
        while loops:
            ttt = TicTacToe()

            for i in range(loops - 1):
                user_input = ttt.cpu_move()
                k, m = user_input
                ttt.update_board(k, m, "O")
            assert ttt.moves == loops - 1

            while ttt.moves < 9:
                cpu_input = ttt.cpu_move()
                i, j = cpu_input  # Return CPU value as coordinates on the board to use index values to update board
                ttt.update_board(i, j, "X")
                if ttt.moves >= 9:
                    ttt.display_board()
                    assert ttt.moves == 9
            loops -= 1
        cpu_moves = ttt.win_condition("X")
        print(ttt.board)
        assert cpu_moves == True

# Test if one of the conditions is met, the function returns True
# Test with a board that is mostly full of X's and O's but there is no tic tac toe


#     # Mock user get_user_input, verify returned value is converted index values
#     @patch("builtins.input", return_value="2")
#     def test_get_user_input(self, mock_get_user_input):
#         ttt = TicTacToe()
# 
#         user_input = ttt.get_user_input()
#         self.assertEqual(user_input, (0, 2))
# 
#     # Mock user input move, run through get_user_input function, pass returned value to update board
#     @patch("builtins.input", return_value="5")
#     def test_get_user_input_move(self, mock_get_user_input):
#         ttt = TicTacToe()
# 
#         user_input = ttt.get_user_input()
#         i, j = user_input
#         ttt.update_board(i, j, "X")
# 
#         self.assertEqual(user_input, (1, 2))
#         assert ttt.display_board()[1][2] == "X"
# 
#     # Mock get_user_input function's input only accepts integer
#     @patch("builtins.input", return_value="A")
#     def test_get_user_input_type_error(self, mock_get_user_input):
#         ttt = TicTacToe()
#         with self.assertRaises(ValueError):
#             user_input = ttt.get_user_input()
# 
# 
# # Test if user input is out of range, it will continue to prompt user for correct range of input
# # Test i, j is only returned if the space is available on the board, i.e. is a valid space


if __name__ == '__main__':
    unittest.main()
