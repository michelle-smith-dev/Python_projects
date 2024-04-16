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
debug = True


def hangman(word):
    # Pick secret word from the provided list
    secret_word = random.choice(word)
    # Keep count of how many guesses have been used
    guess_counter = 0
    # While counter is not more than length of the secret_word + 2, keep prompting user for input
    while guess_counter < len(secret_word) + 2:
        if debug: print(guess_counter)
        if debug: print(len(secret_word) + 2)
        # Create variable to get user input
        guess_letter = str(input("Guess a letter. Hint: It's a type of fruit: "))
        for i in secret_word:
            # if letter is in word, print the word with empty spaces and guess letter position
            if guess_letter == i:
                print("You found a letter!", len(secret_word))
            else:
                guess_counter += 1
                print("Letter not in word.")
    if debug: print(secret_word)

# Stop the for loop if all letters in secret word have been guessed and print word
# Print the location of the letter guessed within the word, i.e. _pp__ for apple
# Can use ascii to print the _ symbol. Could print using length of the secret word.
# Could use if statements, so if secret_word == 'xyz', and then set paths for the code to take and define variables.
# For example, if the secret word is 'pear', (do I create a function named pear to execute), then I when looping through
# the word, I could print a display when they choose a correct letter. Like user chooses a, the code prints variable 'pear_a'
# which outputs '__a_'
# What if I create a function that takes the secret word, and has a bunch of if statements.

fruits = ["orange", "banana", "mango", "apple", "pear", "grapefruit"]
hangman(fruits)