'''Rules of the game
Two players play the game against each other; let’s assume Player 1 and Player 2.

Player 1 plays first by setting a multi-digit number.
Player 2 now tries his first attempt at guessing the number.
If Player 2 succeeds in his first attempt (despite odds which are highly unlikely) he wins the game and is crowned Mastermind! If not, then Player 1 hints by revealing which digits or numbers Player 2 got correct.
The game continues till Player 2 eventually is able to guess the number entirely.
Now, Player 2 gets to set the number and Player 1 plays the part of guessing the number.
If Player 1 is able to guess the number within a lesser number of tries than Player 2 took, then Player 1 wins the game and is crowned Mastermind.
If not, then Player 2 wins the game.'''
# Start the game by first
# Getting user input to guess a 4 digit number

# Keep track of how many guesses the player has guessed.

# Compare the random number with the user input

# If they are equal, break play, store user count of guesses to play against player 2.
# If they guess the number on first try, print they are a mastermind, game ends.

# If number is not guessed, reveal if user got any digits correct, that are in the correct spot. Compare using a
# for loop via indexed values of number guess vs random number

# Repeat code until player is able to guess digit, then break.

# Start game play for player two, will be same as above. Unless a player guessed the number on the first try,
# after second player has guessed the digit, compare the counters for each player to determine winner

import random
debug = True


class Mastermind:

    def __init__(self):
        self.rand_num1 = random.randrange(1000, 10000)
        self.rand_num2 = random.randrange(1000, 10000)
        self.counter1 = 0
        self.counter2 = 0
        self.player = "Player 1"

    # Let's create a director
    def play(self):

        # Call the main game play and pass the self.player variable
        while self.player == "Player 1":
            self.guess_digits(self.player)
            self.player = "Player 2"

        while self.player == "Player 2" and self.counter1 != 0:
            self.guess_digits(self.player)
            self.player = None

        # Calculate how many guesses it took for each player to determine the Mastermind winner
        while self.counter1 != 0 and self.counter2 != 0:
            if self.counter1 > self.counter2:
                print("Player 2 is the Mastermind! They guessed the correct number in", self.counter2, "times.")
            elif self.counter2 > self.counter1:
                print("Player 1 is the Mastermind! They guessed the correct number in", self.counter1, "times.")
            else:
                print("It's a tie! Neither player is a Mastermind.")
            break

    def guess_digits(self, player):

        if player == "Player 1":
            if debug: print("Player 1's random number is:", self.rand_num1)
            while True:
                user_num = self.user_input(player)
                # compare user input to rand_num1
                if user_num == self.rand_num1 and self.counter1 == 0:
                    print("You guessed it right on the first try. Player 1 is the Mastermind!")
                    break
                elif user_num == self.rand_num1:
                    self.counter1 += 1
                    print("You guessed it right in", self.counter1, "guesses!")
                    break
                else:
                    #  Block of code to reveal correct numbers
                    revealed_number = self.reveal_num(user_num, self.rand_num1)
                    self.counter1 += 1
                    print("You did not guess the number, but guessed these numbers right.", revealed_number)

        if player == "Player 2":
            if debug: print("Player 2's random number is:", self.rand_num2)
            while True:
                user_num = self.user_input(player)
                # compare user input to rand_num1
                if user_num == self.rand_num2 and self.counter2 == 0:
                    print("You guessed it right on the first try. Player 2 is the Mastermind!")
                    break
                elif user_num == self.rand_num2:
                    self.counter2 += 1
                    print("You guessed it right in", self.counter2, "guesses!")
                    break
                else:
                    revealed_number = self.reveal_num(user_num, self.rand_num2)
                    self.counter2 += 1
                    print("You did not guess the number, but got these numbers right.", revealed_number)

    def user_input(self, player):
        invalid_inp = True
        while invalid_inp:
            user_num = input(f"{player}, guess a 4 digit number between 1000 - 9999: ")
            if len(user_num) == 4 and user_num.isdigit():
                invalid_inp = False
                return int(user_num)

    def reveal_num(self, user_input, random_number):
        user_list = [int(x) for x in str(user_input)]
        ran_list = [int(x) for x in str(random_number)]
        # print(random_number)
        revealed_number = []
        j = 0
        for i in user_list:
            if i == ran_list[j]:
                revealed_number.append(i)
                j += 1
            else:
                revealed_number.append("_")
                j += 1
        # list_conv = ','.join(map(str, revealed_number))
        return revealed_number


m = Mastermind()
# print(m.user_input())
m.play()