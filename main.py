import random


class PickNumber:
    def __init__(self, games, debug=False):
        self.games = games
        self.debug = debug

    @staticmethod
    def get_usr_inp(prompt):
        usr_inp = ''
        while not usr_inp.isdigit():
            usr_inp = input(prompt)
        return int(usr_inp)

    @staticmethod
    def eval_usr_inp(guess, target):
        if guess == target:
            print("Correct!")
            return True
        else:  # guess != target
            print("Incorrect!")
            return False

    @staticmethod
    def hint_mod(num):
        if num % 2 == 0:
            parity = "even"
        else:  # odd
            parity = "odd"
        print(f"Hint: the number is {parity}!")

    @staticmethod
    def hint_inequality(num, upper):
        if num > upper // 2:
            print(f"The number is greater than {upper // 2}")
        else:
            print(f"The number is less than {(upper // 2) + 1}")

    @staticmethod
    def colorize(text, color):
        i = color
        return str(f'\x1b[{str(i)}m' + text + '\x1b[0m')

    def play(self):
        # get user input and test against valid responses
        usr_inp = input("Play game? ")
        valid_responses = ['yes', 'ya', 'yup', 'sure']
        if usr_inp.lower() not in valid_responses:
            print("Thank you, come again!")
            return  # exit game

        upper = 5
        while True:
            lower = 1
            upper = upper * 2

            # generate random number:
            rand_num = random.randint(lower, upper)
            if self.debug: print(rand_num)  # noqa

            # first guess
            # prompt user and get input
            prompt = f"Pick a number between {lower} and {upper}: "
            usr_inp = self.get_usr_inp(prompt)
            if self.eval_usr_inp(usr_inp, rand_num):
                continue

            # second guess
            # give a hint and get input
            self.hint_mod(rand_num)  # first hint
            usr_inp = self.get_usr_inp(prompt)
            if self.eval_usr_inp(usr_inp, rand_num):
                continue

            # third guess
            # give another hint and get input
            self.hint_inequality(rand_num, upper)  # second hint
            usr_inp = self.get_usr_inp(prompt)
            if self.eval_usr_inp(usr_inp, rand_num):
                continue

            # three incorrect guesses ends the game
            else:
                print(f"{self.colorize('Game Over', 91)}")
                print(f"{self.colorize('Better luck next time!', 92)}")
                break


game = PickNumber(games=3, debug=True)
game.play()