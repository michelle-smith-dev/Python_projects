import random
import string


class RandomGenerator:

    def __init__(self):
        self.user_inp = input('How many characters would you like?')
        self.random_string = ''
        self.characters = (string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)

    def user_gen(self):
        ran = int(self.user_inp)
        for i in range(ran):
            self.random_string += random.choice(self.characters)
        return self.random_string


callMe = RandomGenerator.user_gen()
print(callMe)