# Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.
# prev = 0
# for i in range(1,11):
#     sum = i + prev
#     print('The value of', prev, 'plus', i, 'equals', sum)
#     prev = i

# Write a program to accept a string from the user and display characters that are present at an even index number.
#
# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’

# word = input('What word would you like?')
# print("original word is:", word)
#
# x = list(word)
# for i in x[0::2]:
#     print(i)

# Exercise 4: Remove first n characters from a string
# Write a program to remove characters from a string starting from zero up to n and return a new string.
#
# For Example: remove_chars("pynative", 4) so output must be tive.
# Here, we need to remove the first four characters from a string.
# remove_chars("pynative", 2) so output must be native.
# Here, we need to remove the first two characters from a string.
# Note: n must be less than the length of the string.

# word = input("What is your word?")
# n = int(input("How many letters do you want to remove?"))
# x = list(word)
#
# del x[0:n]
#
# p = ''.join(x)
# print(p)

# #The provided solution:
# def remove_chars(word, n):
#     print('Original string:', word)
#     x = word[n:]
#     return x
#
# print(remove_chars("watermelon", 5))

# # Exercise 5: Check if the first and last number of a list is the same
# # Write a function to return True if the first and last number of a given list is same.
# # If numbers are different then return False.
#
# x = [10, 20, 30, 40, 10]
# y = [75, 65, 35, 75, 30]
# z = [7, 34, 68, 99, 7]
#
#
# def compare(lists):
#     if lists[0] == lists[-1]:
#         print("Result is True")
#     else:
#         print("Result is False")
#
#
# c = [x, y, z]
#
# def get_imp(list_of_lists):
#     prompt = 'Type "info" to get commands. Type "exit" to exit out of program. > '
#     usr_inp = None
#     while True:
#         n = len(list_of_lists)
#         usr_inp = input(prompt)
#         if usr_inp == 'exit':
#             break
#         elif usr_inp == 'info':
#             n = len(list_of_lists)
#             [print(str(i) + ':', list_of_lists[i]) for i in range(n)]
#         elif usr_inp.isdigit() and int(usr_inp) in range(n):
#             compare(list_of_lists[int(usr_inp)])
#         else:
#             print('invalid command')
#
#
# get_imp(c)



# # Exercise 6: Display numbers divisible by 5 from a list
# # Iterate the given list of numbers and print only those numbers which are divisible by 5
#
# j = [10, 20, 33, 46, 55, 105, 255, 78]
#
#
# def div(lists):
#     for i in lists:
#         if i % 5 == 0:
#             print(i)
#         else:
#             print("Nope")
#
#
# div(j)

# Exercise 7: Return the count of a given substring from a string. Write a program to find how many times substring “Emma” appears in the given string.
# Given: str_x = "Emma is good developer. Emma is a writer"
# Expected Output: Emma appeared 2 times
"""
Sudo code:
define variable str_x with provided sentence.
create a new variable with str_x using the split method.
create a function to loop over the split variable, looking for the word Emma.
create a new list to contain all the found Emma words.
Use len of list to return count and print the word plus the length of the created new list.
"""

# str_x = "Emma is good developer. Emma is a writer"
# x = str_x.split()
#
#
# def count_words():
#     for i in x:
#         m = ''
#         if i == 'Emma':
#             m += 'Emma'
#             print(m)
#
#
# count_words()

# Their solution:
'''
def count_emma(statement):
    print("Given String: ", statement)
    count = 0
    for i in range(len(statement) - 1):
        count += statement[i: i + 4] == 'Emma'
    return count

count = count_emma("Emma is good developer. Emma is a writer")
print("Emma appeared ", count, "times")'''

# # Exercise 8: Print the following pattern
# # 1
# # 2 2
# # 3 3 3
# # 4 4 4 4
# # 5 5 5 5 5
# # Write a for loop to iterate over a value and concatenate the values using list comprehension
# for num in range(1, 6):
#     for i in range(num):
#         print(num, end=" ")
#     print("\n")
'''
Exercise 9: Check Palindrome Number
Write a program to check if the given number is a palindrome number.

A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers
'''
# inp = input("Provide a 3 digit number: ")
# list1 = list(inp)
#
#
# def pal(lis):
#
#     lis[0], lis[-1] = lis[-1], lis[0]
#     return lis
#
#
# def compare(val):
#     # conv = ""
#     # for i in range(len(val)):
#     #     conv += val[i]
#     conv = "".join(val)
#     print(conv)
#     print(inp)
#     if conv == inp:
#         print("Yes, this is a palindrome number.")
#     else:
#         print("No, this is not a palindrome number.")
#
#
# compare(pal(list1))

'''
Exercise 10: Create a new list from two list using the following condition
Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers from 
the first list and even numbers from the second list.
loop through each list, appending the odd numbers from list1 and even numbers from list2 into a new list; can use
modulo odd/even test
'''

# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# new_list = []
#
#
# def odd(val):
#     # new_list = []
#     for i in val:
#         if i % 2 == 1:
#             new_list.append(i)
#
#
# def even(val):
#     for i in val:
#         if i % 2 == 0:
#             new_list.append(i)
#     print(new_list)
#
#
# odd(list1)
# even(list2)

'''
Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.
I know I'll need a variable with an empty string, this can be what I assign the extracted digit to.
Loop over the integer and start at -1 index?
'''


# def rev(val):
#     reverse_list = []
#     for i in val[::-1]:
#         reverse_list.append(i)
#     conv = " ".join(reverse_list)
#     return conv
#
#
# print(rev(str(7536)))

'''
Below is their solution. Running it through the debugger, I understand that since modulo is the remainder, when dividing
against 10, the remainder will always be the last number. So that's why they can assign it to the digit they want to keep.
Then floor division because it rounds down, doing it against 10, drops the last number and they repeat looping over the full
number until complete. Ingenious.
'''
# number = 7536098
# print("Given number", number)
# while number > 0:
#     # get the last digit
#     digit = number % 10
#     # remove the last digit and repeat the loop
#     number = number // 10
#     print(digit, end=" ")

# '''
# Exercise 12: Calculate income tax for the given income by adhering to the rules below
# Taxable Income	Rate (in %)
# First $10,000	0
# Next $10,000	10
# The remaining	20
#
# Expected Output:
# For example, suppose the taxable income is 45000, and the income tax payable is
# 10000*0% + 10000*10%  + 25000*20% = $6000.
# '''
#
#
# def taxes(income_amount):
#     if income_amount >= 20000:
#         high_tax = income_amount - 20000
#         taxes_owed = 10000*0.10 + high_tax*0.20
#     elif income_amount >= 10000:
#         mid_tax = income_amount - 10000
#         taxes_owed = mid_tax*0.10
#     else:
#         taxes_owed = 0
#     print("Taxes owed:", taxes_owed)
#
#
# taxes(int(input("What is your income?")))


# # Exercise 13: Print multiplication table from 1 to 10
# '''
# Write a loop that loops over a range of 1, 11 to get 1 to 10,
# multiply each iteration times itself over a range of 1, 11
# '''
#
# for i in range(1, 11):
#     for j in range(1, 11):
#         mult = i * j
#         print(mult, end=' ')
#     print()


# print(int(0b1011))
# print(bin(42))

