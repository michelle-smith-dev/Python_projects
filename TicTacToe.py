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
        self.moves = 0

    def run(self):
        while True:

            self.display_board()  # Display board at start of game and after each round of turns

            user_input = self.get_user_input()  # Get user input, check if it's valid and convert
            i, j = user_input  # Return user input as coordinates on the board to use index values to update board
            self.update_board(i, j, "X")  # Pass converted number to update the board
            if self.win_condition("X") is True:  # Pass updated board to win condition
                self.display_board()
                print("Congratulations, you win!")
                break

            if self.moves >= 9:  # Check if all 9 moves have been made without anyone winning
                print("Cat Wins!")
                break

            cpu_input = self.cpu_move()  # CPU Move
            i, j = cpu_input  # Return CPU value as coordinates on the board to use index values to update board
            self.update_board(i, j, "O")  # Update CPU Move
            if self.win_condition("O") is True:  # Check if computer has won
                self.display_board()
                print("You Lose. Computer Wins.")
                break

    def get_user_input(self):
        # Check that input is a valid number between 0 - 8 and is available on the board
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

    def update_board(self, val1, val2, player: str):
        if not isinstance(player, str):
            raise TypeError
        self.board[val1][val2] = player  # Update board with player's X or O
        self.moves += 1

    def cpu_move(self):
        # Generate random input to run through the converter based on list values not 'X'
        while True:
            y = random.choice(range(9))
            i, j = self.convert_to_ij(y)
            if self.board[i][j] == y:
                return i, j

    def win_condition(self, player):
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
# ttt.run()
