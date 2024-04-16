import random

def hangman(word):
    # Pick secret word from the provided list
    secret_word = random.choice(word)
    # Keep count of how many guesses have been used
    guess_counter = 0
    # While counter is not more than length of the secret_word + 2, keep prompting user for input
    while guess_counter < len(secret_word) + 2:
        guess_letter = str(input("Guess a letter. Hint: It's a type of fruit: "))
        if secret_word == "pear":
            if guess_letter == "p":
                print("p___")
            if guess_letter == "e":
                print("_e__")
            if guess_letter == "a":
                print("__a_")
            if guess_letter == "r":
                print("___r")
            else:
                guess_counter += 1

        elif secret_word == "apple":
            if guess_letter == "a":
                print("a____")
            if guess_letter == "p":
                print("_pp__")
            if guess_letter == "l":
                print("___l_")
            if guess_letter == "e":
                print("____e")
            else:
                guess_counter += 1


# fruits = ["orange", "banana", "mango", "apple", "pear", "grapefruit"]
fruits = ["pear", "apple"]
hangman(fruits)