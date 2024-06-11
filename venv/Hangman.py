import random

'''
Choose a random word from a list of secret words to be the word guessed by user.
This will use the random function.
If a letter has been guessed correctly, reveal that letter in it's correct position of the word.
Allow the length of word + 2 guesses
'''

'''
Let's walk through it conceptually:
I need to create a list of "secret words", this will be passed to the hangman function.
Create hangman function to pass the secret word, and then using random function, store word as a variable.
I will need to get user input to guess a letter. This will have a limit of random word + 2, so while this limit has not been hit,
prompt user for input to guess a letter. Will have to keep count.
If user can guess word, allow user to enter word in prompt, compare word with the variable and print.
Loop over the secret word to see if the letter guess is in the word. If yes, print, if no, print not in word, and deduct
from counter of uses.
'''
debug = False

class hangman():

    def __init__(self):
        self.secret_word = random.choice(["orange", "banana", "mango", "apple", "pear", "grapefruit", "strawberry", "blueberry", "kiwi", "starfruit"])
        if debug: print("Secret word:", self.secret_word)
        self.incorrect_guess_counter = 0
        self.w_display = []
        for j in range(len(self.secret_word)):
            self.w_display.append('_')  # Fill w_display with blank underscores based on length of secret word
        self.letters_guessed = []

    # @staticmethod
    # def word_display(self):
    #     w_display = []
    #     for j in range(len(self.secret_word)):
    #         self.w_display.append('_')
    #     return w_display

    def play_game(self):
        # Display blank word at start of game
        self.display_blank_word()

        while True:

            # Prompt user for user_input to get letter
            guess_letter = self.get_user_input()
            if debug: print(guess_letter)

            # Pass letter to find_letter function to determine if letter is in word
            # If letter is found in word, display board with letter(s) in proper place
            if self.find_letter(guess_letter) is True:
                self.display_hangman_board(guess_letter)
            else:
                self.incorrect_guess_counter += 1  # Add the guess to counter
                print("Letter not found or already guessed.")

            # Check if word is complete "win function"
            if self.win_hangman() is True:
                print("\nYOU WIN!")
                break

            # Check how many guesses have been made
            if self.incorrect_guess_counter >= 6:
                print("\nYou lose :(")
                break

    def display_blank_word(self):
        if debug: print(self.secret_word)
        for i in range(len(self.secret_word)):  # Get length of the secret_word and loop over it, displaying _
            print('_', end=' ')

    def get_user_input(self):
        g_letter = str(input("\nGuess a letter. Hint: It's a type of fruit: "))
        return g_letter

    def find_letter(self, letter):
        for i in self.secret_word:  # Loop over the secret word and look for the guessed letter.
            if i == letter and i not in self.letters_guessed:
                self.letters_guessed.append(letter)
                return True

    def display_hangman_board(self, letter):
        n = 0  # Use as placeholder for index value
        for i in self.secret_word:
            if i == letter:
                self.w_display[n] = i  # Replace index value with the letter
                n += 1  # Increase index value as you loop through
            else:
                n += 1  # Increase index value as you loop through
        # for i in self.w_display:
        #     print(i, end=' ')
        print("displayed word:", self.w_display)

    def win_hangman(self):
        # Loop over the secret word and determine if a '_' exists. If it doesn't, return True
        win = 0
        for i in self.w_display:
            if i == '_':
                win += 1
        if debug: print("How many underscores:", win)
        if win == 0:
            return True


'''
display blank word
get user input
check if letter provided is in word
if letter is in word, display word with letters in correct location and prompt for user input
if letter is not in word, prompt for user input [eventually display hangman parts]
continue to prompt for user input until word is filled or all moves have been used, and end game
win or lose function
'''
# Stop the for loop if all letters in secret word have been guessed and print word
# Print the location of the letter guessed within the word, i.e. _pp__ for apple
# Can use ascii to print the _ symbol. Could print using length of the secret word.
# Could use if statements, so if secret_word == 'xyz', and then set paths for the code to take and define variables.
# For example, if the secret word is 'pear', (do I create a function named pear to execute), then I when looping through
# the word, I could print a display when they choose a correct letter. Like user chooses a, the code prints variable 'pear_a'
# which outputs '__a_'
# What if I create a function that takes the secret word, and has a bunch of if statements.

# fruits = ["orange", "banana", "mango", "apple", "pear", "grapefruit"]
hang = hangman()
# hang.display_hangman_board("o")
# hang.play_game()
# hang.display_blank_word()
