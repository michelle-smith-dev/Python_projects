# # start app
# # show board
# # prompt for user input
# # check that is valid
# # apply user input
# # check for win condition on state change
# # show updated board
# # random cpu choice
# # check that it is valid
# # check for win condition on state change
# # show updated board
import random


class TicTacToe:

    def __init__(self):
        self.board = [[0, 1, 2],
                      [3, 4, 5],
                      [6, 7, 8]]
        self.x_player = []
        self.comp_player = []

    def run(self):
        # self.is_player_turn = True
        while True:
            # Display board
            self.display_board()
            # Get user input, check if it's valid and convert
            user_input = self.get_user_input()
            i, j = user_input
            # Pass converted number to update the board
            self.update_board(i, j, "X")
            # Pass updated board to win condition
            if self.win_condition("X") is True:
                print("Congratulations, you win!")
                break
            # CPU Move
            cpu_input = self.cpu_move()
            i, j = cpu_input
            # Update CPU Move
            self.update_board(i, j, "O")
            # Check if computer has won
            if self.win_condition("O") is True:
                print("You Lose. Computer Wins.")
                break

    def get_user_input(self):
        # Check that input is a valid number between 0 - 8, store used numbers from both users
        # Check that number is available on the board
        while True:
            user_input = int(input("Where do you want to put your 'X'?: "))
            if user_input in range(9):
                i, j = self.convert_to_ij(user_input)
                if self.board[i][j] == user_input:
                    return i, j

    @staticmethod
    def convert_to_ij(number):
        i = number // 3
        j = number % 3
        return i, j

    def update_board(self, val1, val2, player):
        if player == 'X':
            self.x_player.append([val1, val2])
        else:
            self.comp_player.append([val1, val2])
        self.board[val1][val2] = player

    def cpu_move(self):
        # Generate random input to run through the converter based on list values not 'X'
        while True:
            y = random.choice(range(9))
            i, j = self.convert_to_ij(y)
            if self.board[i][j] == y:
                return i, j

    def win_condition(self, player=None):
        horizontal_top = self.board[0][0] == player and self.board[0][1] == player and self.board[0][2] == player
        horizontal_mid = self.board[1][0] == player and self.board[1][1] == player and self.board[1][2] == player
        horizontal_bottom = self.board[2][0] == player and self.board[2][1] == player and self.board[2][2] == player
        vertical_left = self.board[0][0] == player and self.board[1][0] == player and self.board[2][0] == player
        vertical_mid = self.board[0][1] == player and self.board[1][1] == player and self.board[2][1] == player
        vertical_right = self.board[0][2] == player and self.board[1][2] == player and self.board[2][2] == player
        diag_top_left = self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player
        diag_top_right = self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player
        if horizontal_top or horizontal_mid or horizontal_bottom or vertical_left or vertical_mid or vertical_right or diag_top_left or diag_top_right:
            return True
        else:
            return False

    def display_board(self):
        for grid in self.board:
            print(*grid, sep='|')
        return self.board


ttt = TicTacToe()
ttt.run()
