# string builder demo

# how to construct a random string generator?

# I want a random string of 5 characters...
import random
import string
# # string.ascii_lowercase
# # string.ascii_uppercase
# usr_inp = int(input('What size would you like your string to be?'))
# # usr_inp = int(usr_inp)
# print('create string of', usr_inp, 'long')
# # Pick the number of characters you need, one at a time.
#
# random_string = ''
# for i in range(usr_inp):
#     random_string += random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)
#
# print(random_string)


# class RandomGen:
#     def __init__(self, user_inp, chars, random_string):
#         self.user_inp = user_inp
#         self.chars = chars
#         self.random_string = random_string
# #        self.user_inp = int(input('What size would you like your string to be?'))
# #        self.chars = random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits)
#
#     def gen1(self):
#         for i in range(self.user_inp):
#             RandomGen.random_string = ''
#             RandomGen.random_string += RandomGen.chars
#             return
#
#
# print(RandomGen.random_string)
#
# RandomGen.user_inp = int(input('What size would you like your string to be?'))
# RandomGen.chars = random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits)


#### Prompts for user input, but doesn't randomize value instead of the full amount ###
# class RandomGen:
#
#     random_string = ''
#     chars = random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits)
#
#     def __init__(self):
#         self.user_inp = int(input('What size would you like your string to be?'))
#
#     def gen1(self):
#         for i in range(self.user_inp):
#             RandomGen.random_string += RandomGen.chars
#         return None
#
#
# input1 = RandomGen()
# input1.gen1()
# print(RandomGen.random_string)


### Scott's suggestions ####

class RandomGen:

    def __init__(self):
        self.user_inp = int(input('What size would you like your string to be?'))
        self.random_string = ''

    def get_input(self):
        for i in range(self.user_inp):
            self.random_string += random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits)
        return self.random_string


# input1 = RandomGen()
# print(input1.get_input())
print_me = RandomGen().get_input()
print(print_me)


