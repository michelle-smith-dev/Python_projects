
# # Problem A (optional)
# my_list = []
# for x in range(3):
#     for y in range(2):
#         xy_tuple = (x, y)
#         my_list.append(xy_tuple)
#
# print(my_list)
# # Write out the contents of my_list.
# # list should be: xy_tuple = (0, 0, 0, 1, 1, 0, 1, 1, 2, 0, 2, 1)
# # missed it being nested

# # Problem B (optional)
# my_list = []
# for x in range(1):
#     for y in range(3):
#         xy_tuple = (x, y)
#         my_list.append(xy_tuple)
#
# print(my_list)
# # Write out the contents of my_list.
# # my_list = [(0, 0), (0, 1) (0, 2)]

# # Problem C (optional)
# my_list = []
# for x in range(0):
#     for y in range(3):
#         xy_tuple = (x, y)
#         my_list.append(xy_tuple)
#
# print(my_list)
# # Write out the contents of my_list.
# # my_list = []

# # Problem D (optional)
# my_list = []
# for x in range(3):
#     for y in range(0):
#         xy_tuple = (x, y)
#         my_list.append(xy_tuple)
#
# print(my_list)
# # Write out the contents of my_list.
# # my_list = []

# # Problem E (optional)
# my_list = []
# for x in range(2):
#     for y in range(4):
#         xy_tuple = (x, y)
#         my_list.append(xy_tuple)
#
# print(my_list)
# # Write out the contents of my_list.
# # my_list = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1,), (1, 2), (1, 3)]

# # Problem 1
# others = 0
# for i in range(3):
#     for j in range(1):
#         if i == j:
#             others += 1
# else:
#      others += 1
# print(others)
# # Others = 2

# # Problem 2
# # Write out each iteration's i and j values, and any changing variables
# # Include changes from any else clause(s)
#
# foo = 0
# for i in range(2):
#     for j in range(3):
#         if i < j:
#             foo += 1
#     else:
#          foo += 1
#
# print(foo)
# # What is foo? 0 < 0, 0 < 1, 0 < 2, +2 foo
# # 1 < 0, 1 < 1, 1 < 2, +1 foo
# # foo = 5

# Problem 3
# Write out each iteration's i and j values, and any changing variables
# Include changes from any else clause(s)

# bar = 0
# for i in range(3):
#     for j in range(4):
#         if i < j:
#             bar += 1
#         else:
#             bar -= 1
# print(bar)
# # What is bar?
# # 0 < 0, 0 < 1, 0 < 2, 0 < 3 bar = 2
# # 1 < 0, 1 < 1, 1 < 2, 1 < 3 bar = 2
# # 2 < 0, 2 < 1, 2 < 2, 2 < 3
# # bar = 0

# # Problem 4
# # Write out each iteration's i and j values, and any changing variables
# # Include changes from any else clause(s)
#
# baz = 0
# for i in range(3):
#     for j in range(2):
#         if i > j:
#             baz += 1
#         else:
#             baz -= 1
# else:
#     baz = 0
#
# print(baz)
# # What is baz?
# # 0 > 0, 0 > 1 bar =
# # It will hit the else statement
# # baz = 0

# # Problem 5
# # Write out each iteration's i and j values, and any changing variables
# # Include changes from any else clause(s)
#
# var = 0
# for i in range(1):
#     for j in range(4):
#         if i != j:
#             var += 1
#         else:
#             var -= 1
# else:
#     var *= 2
#
# # what is var?

# # Problem 6
# # Write out each iteration's i and j values, and any changing variables
# # Include changes from any else clause(s)
#
# ven = 0
# for i in range(1):
#     for j in range(4):
#         if i != j:
#             ven += 1
#     else:
#         ven += 1
# else:
#     ven += 1
#
# # what is ven?

# # lst = [[x for x in range(3)] for y in range(3)]
# #
# # for r in range(3):
# #     for c in range(3):
# #         if lst[r][c] % 2 != 0:
# #             print("#")
#
# ray = [[x for x in range(3)] for y in range(3)]
# yay = [[0, 1, 2] for y in range(3)]
# print(yay)

# dct = {}
# dct['1'] = (1, 2)
# dct['2'] = (2, 1)
#
# for x in dct.keys():
#     print(dct[x][1], end="")

# def fun(x):
#     if x % 2 == 0:
#         return 1
#     else: return 2
#
#
# print(fun(fun(2)))

# var = 2
# for i in range(2):
#     for j in range(3):
#         if i == j:
#             var += 1
#     else:
#         var += 1
# else:
#     var += 1
#
# # What is var? 1, 1, 1, 1, 1
# # var = 5 + 2 = 7
# print(var)

# tup = (2, 4, 6, 8)
# tup = tup[-2: -1]
# tup = tup + tup
# print(tup)

# tup = (1, 3, 5, 7)
# tup = (1, 2, ) + tup[-3:-1]
# print(tup)

# var = 3
# for i in range(3):
#     if i < 3:
#         break
#     var -= 1
# else:
#     var -= 1
#
# # var = 3
# print(var)

# var = 1
# for x in range(4):
#     if x < 3:
#         continue
#     var += 1
# # var = 2
# print(var)

# def fn(y):
#     if y % 2 == 1:
#         return 2
#     else:
#         return 1
#
#
# print(fn(fn(2)))
# # 2

# z = ['a' for i in range(4)] # ['a', 'a', 'a', 'a']
#
# for each in z:
#     print(each + each, end=' ')

# f = [3+i for i in range(3)] # [3, 4, 5]
#
# for j in f:
#     print(j-j*2) # 3 - 6 = -3, 4 - 8 = -4, 5 - 10 = -5
#
# # -3, -4, -5

# 5//2 = 2
# 5 % 2 = 1

# def fn(n):
#     if n == 0:
#         return 1
#     return fn(n-1)
# print(fn(3))
# # 1

# foo = {'b': 2, 'c': 3, 'd': 4}
# print(foo.keys())
# print(foo.values())
# print(foo)
# print(foo['c'])
#
# try:
#     print(0 + 3/0)
# except ValueError:
#     print('a')
# except ZeroDivisionError:
#     print('b')
# except:
#     print('c')

#ZeroDivisionError, 'b'

# 1. 33 ** 0 + 5 -> 6 // any number raised to 0 is always 1
# 2. 12 % 37 -> 12
# 3. 5 % 2 -> 1
# 4. 5 // 2 -> 2

# try:
#     0/1
#     int('foo')
#     [].update()
# except AttributeError:
#     print('a')
# except ZeroDivisionError:
#     print('b')
# except ValueError:
#     print('c')
# # ValueError

# 1)
# for i in range(4):
#     print(i)
# # Will print: 0, 1, 2, 3

# # 2)
# for i in range(2):
#     for j in range(3):
#         print(i,j)
#     break
# # 0, 0
# # 0, 1
# # 0, 2

# # 3)
# for i in range(2):
#     for j in range(3):
#         for k in range(1):
#             print(k, j, i)
#         break
# else:
#     print('bar')
# # 0 0 0
# # 0 0 1
# # bar

# # 4)
# # total is 5
# x = input()
# y = input()
# # type error

# #5)
# my_tupe = (1, 2, 3)
# # my_tupe[1] = 0 # you can't change a tuple so assignment doesn't work
# my_tupe = my_tupe[1] + my_tupe[0] # 3
# print(my_tupe)

# # 6)
# a = 1
# b = 0
# a = b ^ a
# b = a ^ b
# a = a ^ b
# print(a,b) # 0, 1
#
# # 7)
# c = 0
# d = 1
# d = c & d
# c = c | d
# d = c & d
# print(d) # 0

# # 8)
# def fn(n):
#     if n % 2 == 1:
#         return 1
#     return n % 2
#
#
# print(fn(fn(3))) # 1
#
# # 9)
# print('a', 'b', sep='end') # aendb
#
# # 10)
# print('b', 'a', end='sep') # b asep

# # 11)
# def fun(go, x=0, y=0):
#     if go:
#         print(x,y)
#     else:
#         print(go,x,y)
#
#
# print(fun(False,1))  # False, 1, 0
z = [[0,1,2], [0,1,2], [0,1,2]]
for i in z:
    for j in i:
        if z[i][j] == 1:
            print('f')
        # print(i,j)
        # if i == j:
        #     print('f')
