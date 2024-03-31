# # names = ['frank', 'jan', 'bob', 'judy']
# #
# # for name in names:
# #     if len(name) == 3:
# #         print(name)
# #
# # for char in 'stan':
# #     print(char)
#
# # name = 'stan'
# # for i in [0, 1]:
# #     print(name[i])
#
# # lst = [1, 2, 3, 4, 5, 6, 7, 8]
# # for i in range(1, len(lst)//2 + 1):
# #     lst[i -1], lst[-i] = lst[-i], lst[i -1]
# #
# # print(lst)
#
#
# # while condition_true:
# #   do this; always requires break statements so it doesn't get stuck in an infinite loop
#
# # x = 0
# # while x < 3:
# #     print(x)
# #     x = x + 1  # will print 0, 1, 2: because it's reading while x is less than 3 and
#     # will loop until it becomes equal to 3, or until the while statement is no longer true.
#
# # y = 6
# # while y > 3:
# #     print(y)
# #     y -= 1
# #     if y % 2 == 0:
# #         break
#
# # for i in [0, 1, 2, 3, 4, 5]:
# #     if i % 2 == 0:
# #         continue
# #     print(i)
# #     if i > 2:
# #         break
#
# # it1 is abc
# # it2 is 123
# # then it should break
# # then continue to print the full each
#
# # for each in ['abc', '123', 'defg', 'hi']:
# #     if len(each) <= 3:
# #         print(each)
# #     else:
# #         break
# #     continue
# #     print(each)  # this code is unreachable because there's a continue before it
#
# # my_list = [5, 10, 15]
# # my_other_list = ['a', 'b', 'c']
# #
# # my_dictionary = {}
# #
# # iter_count = len(my_list)
# #
# # for i in range(iter_count):
# #     my_dictionary[my_other_list[i]] = my_list[i]
# #
# # print(my_dictionary)
#
# # x = {'a': 1, 'b': 5}
# # adder = 0
# # for i in x.values():
# #     adder += i
# # print(adder)
#
# # loops = 0
# # while loops < 3:
# #     print("I'm looping... ")
# #     print("I've looped", loops, "times!")
# #     loops = loops + 1
#
# # size = 5
# # my_list = list()
# # while size > 0:
# #     my_list.append(5)
# #     size = size - 1
# # print(my_list)
#
# # stop = 11
# # number = 0
# # while number < stop:
# #     number += 1
# #     if number % 2 == 1:
# #         continue
# #     print(number)
# # #    number += 1
#
# # names = ['jane', 'bob', 'judy', None, 'frank']
# #
# # length = len(names)
# # i = 0
# # while i < length:
# #     next_name = names[i]
# #     next_type = type(next_name)
# #     if next_type is not str:
# #         break
# #     print(names[i], 'is a valid name!')
# #     i += 1
#
# # i = 0
# # while i < 4:
# #     i += 1
# #     print(i)
# # else:
# #     print('hello')
# #
# # for each in range(3):
# #     if each ** 2:
# #         print(each)
#
# # my_list = [1, 2, 3]
# # for v in range(len(my_list)):
# #     my_list.insert(1, my_list[v])
# # print(my_list)
#
# # var = 0
# # while var < 6:
# #     var += 1
# #     if var % 2 == 0:
# #         continue
# #     print("#")
#
# # Take the Else path
# # i = 0
# # while i < 3:
# #     i = i + 1
# #     if i > 6:
# #         break
# #     print(i)
# # else:
# #     print('do things')
#
# # Does not take the Else path
# # i = 0
# # while i < 4:
# #     i += 1
# #     if i == 3:
# #         break
# #     print(i)
# # else:
# #     print('hello')
#
# # for i in range(3):
# #     for j in range(2):
# #         print(i,j)
#
# # Bubble Sort
# x = [6, 5, 2, 1, 7]
# n = len(x)

# for m in range(n):
#     for i in range(n-1):
#         if x[i] > x[i+1]:
#             x[i], x[i+1] = x[i+1], x[i]
#
# print(x)


# income = float(input("Enter the annual income: "))
# inc_minus = 556.02
# percent = 0.18
#
# if income < 85528:
#     income * percent - inc_minus = tax
#
# tax = round(tax, 0)
# print("The tax is:", tax, "thalers")


# def walk(top):
#     if top == 0:
#         return 0
#     else:
#         return top * walk(top - 1)
#
#
# print(walk(2))

# the_list = ['a', 'b', 'c']
# counter = 0
# for ix in range(len(the_list)):
#     print(the_list[ix], end=' ')
#     the_list[ix] = counter
#     counter += 2
# for ix in range(len(the_list)):
#     print(the_list[ix], end=' ')

# def process(data):
#     data = [1, 2, 3]
#     return data[-2]
#
#
# measurements = [0 for i in range(3)]
# process(measurements)
# print(measurements[-2])
# #
# #
# def process(data):
#     data[1] = 2
#     return data[-2]
#
#
# measurements = [0 for i in range(3)]
# process(measurements)
# print(measurements[-2])

# for i in range(1):
#     print("#")
# else:
#     print("#")

# t = [[3-i for i in range (3)] for j in range (3)]
# s = 0
# # r = [3-i for i in range (3)] = [3, 2, 1] [3, 2, 1] [3, 2, 1]
# for i in range(3):
#     s += t[i][i]
# print(s)

# def any():
#     print(var + 1, end='')
#
#
# var = 1
# any()
# print(var)

# others = 1
# for i in range(2, 4):
#     for j in range(-1, 2):
#         if i == j:
#             others += 1
#         else:
#             break
# print(others)

# x = [{'a': i, 'b': i+2} for i in range(2)]
# y = 1
# z = 'b'
# print(x[y][z])

my_var = []
for i in range(4):
    while i > 0:
        i -= 1
        my_var.append(i)

print(my_var)


