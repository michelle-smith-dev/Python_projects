import unittest
# import TicTacToe
from TicTacToe import TicTacToe

class MyTestCase(unittest.TestCase):

    # def test_run_method(self):


    def test_update_board(self):
        update = TicTacToe()

        # Test updating the board is actually updated with an X or an O
        update.update_board(0, 1, "X")
        assert update.display_board()[0][1] == "X"
        update.update_board(2, 1, "O")
        assert update.display_board()[0][1] == "X"

        # Test when update board is ran, the moves variable adds +1 for each update_board move
        assert update.moves == 2

        # Test invalid index parameters raises an exception
        with self.assertRaises(IndexError):
            update.update_board(3, 1, "X")
        with self.assertRaises(IndexError):
            update.update_board(2, 4, "O")
        with self.assertRaises(TypeError):
            update.update_board("hello", 1, "O")

        # Test filling the board with O's
        m, n = 0, 0
        for ele_m in range(3):
            for ele_n in range(3):
                # print(ele_m, ele_n)
                update.update_board(m, n, "O")
                assert update.board[m][n] == 'O'
                if ele_m == 2 and ele_n == 2:
                    break
                n += 1
            m += 1
            n = 0

    def test_convert_to_ij(self):

        # Test function can convert integers successfully
        self.assertEqual(TicTacToe.convert_to_ij(8), (2, 2))
        self.assertEqual(TicTacToe.convert_to_ij(0), (0, 0))
        self.assertEqual(TicTacToe.convert_to_ij(4), (1, 1))
        self.assertEqual(TicTacToe.convert_to_ij(-1), (-1, 2))
        self.assertEqual(TicTacToe.convert_to_ij(1022), (340, 2))
        self.assertEqual(TicTacToe.convert_to_ij(1.22), (0.0, 1.22))

        # Test function raises an error when integer is not passed
        with self.assertRaises(TypeError):
            TicTacToe.convert_to_ij("Hello")

    def test_cpu_move_blank_board(self):

        ttt = TicTacToe()
        cpu_move = ttt.cpu_move()

        # Test i, j is in valid range
        i, j = 0, 2
        result = False
        for element in cpu_move:
            if element >= i and element <= j:
                result = True
                print(element)
                break

        assert result == True

        # Loop the cpu_move until all values on the board have been chosen
        move = False
        while ttt.moves < 9:
            cpu_input = ttt.cpu_move()
            i, j = cpu_input  # Return CPU value as coordinates on the board to use index values to update board
            ttt.update_board(i, j, "X")
            if ttt.moves >= 9:
                move = True
                ttt.display_board()

        assert move == True

    # Start with board having 1 move on it, and verify cpu_move can fill remaining board
    # def test_cpu_move_filled_board(self):
    #     ttt = TicTacToe()
    #     # cpu_move = ttt.cpu_move()
    #     m, n = 0, 0  # I want [0, 0][0, 1][0, 2][1, 0][1, 1][1, 2][2, 0][2, 1]
    #     for ele_m in range(3):
    #         for ele_n in range(3):
    #             # print(ele_m, ele_n)
    #             ttt.update_board(m, n, "O")
    #             while ttt.moves < 9:
    #                 cpu_input = ttt.cpu_move()
    #                 i, j = cpu_input  # Return CPU value as coordinates on the board to use index values to update board
    #                 ttt.update_board(i, j, "X")
    #                 if ttt.moves >= 9:
    #
    #             if ele_m == 2 and ele_n == 2:
    #                 break
    #             n += 1
    #         m += 1
    #         n = 0
    #
    #     assert ttt.board[0][0] == 'O'
        # move1 = False
        # while ttt.moves < 9:
        #     cpu_input = ttt.cpu_move()
        #     i, j = cpu_input  # Return CPU value as coordinates on the board to use index values to update board
        #     ttt.update_board(i, j, "X")
        #     if ttt.moves >= 9:
        #         move1 = True
        #         ttt.display_board()
        #
        # assert move1 == True

        # Test boundaries by populating the board and then running the cpu_move and make sure it eventually picks the correct index
        # Test more boundaries by populating with a couple, then with mid, like 5 and test to make sure it hasn't picked
        # a used value on the board

        # Loop over the cpu_move a hundred times, maybe put the above for loop in a while loop to make it run several times

# # test if random number is not valid, the while loop will run until a valid number is chosen


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
