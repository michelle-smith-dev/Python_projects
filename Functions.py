# # error handling
# inp = input('pls give num:')
# try:
#     inp = int(inp)
#     print(inp ** 2)
# except:
#     print('bad value')

# # Another try/except example to show different except errors. Can do 1/0 to get a different except error
# try:
#     '1'/'0'
# except ZeroDivisionError:
#     print('no zero')
# except ValueError:
#     print('bad value')
# except:
#     print('neither zero or value error')

# # Run this by yourself // will return unsupported type error
# '1'/'0'

# # Re-raises the last error that was active in the current scope (need to play/research this more)
# raise ValueError

# ### RECURSION ###
# recursive functions: a function that calls itself
# base case(s): have some terminating condition; will always be at the top, before the recursive case.
# In the example below, the base case(s) is the if a > 10 statement
# recursive case(s): get closer to base case; ex. reducing input size [where you call yourself]

# # example of recursive, which runs forever
# def adder(a):
#     print(a)
#     return adder(a + 1)
#
# adder(3)

# # example of base case(s) recursive function
# def adder(a):
#     print(a)
#     if a > 10:
#         print('base case reached!')
#         return None
#     return adder(a + 1)
#
# adder(1)

# # factorial
# def fn2(param=1):
#     #do things
#     return
#
#
# fn2()

# # Can you use a try/except to test a function?
# def fun(x):
#     for i in range(x):
#         y = i*2
#     return y
#
# try:
#     y = fun(5)
# except AttributeError:
#     y = 1
# except TypeError:
#     y = 2
# except ValueError:
#     y = 3
# except ZeroDivisionError:
#     y = 4
# except:
#     y = 5


# def fun(x):
#     for i in range(5):
#         y = i*2
#     return y
#
#
# fun(a=1)

# n = 101
# total = 0
# for i in range(n):
#     total = total + i
#
# print(total)

# my_list = [2, 4, 6]


# def my_function(m):
#     thing = []
#
#     for i in m:
#         a = i % 2 == 0
#         thing.append(a)
#
#     return thing
#
#
# foo = my_function(my_list)
#
# print(foo)

# def factorial(n):
#     #base case
#     if n < 1:
#         return 1
#
#     #recursive case
#     return n * factorial(n - 1)
#
#
# print(factorial(3))

# ### A good way to look at recursive functions ###
#
# def fun(n):
#     if n < 1:
#         return 1
#     return fun(n-1) + n
#
#
# print(fun(3))
#
# # Solution:
# # f(3) = f(2) + 3
# # f(2) = f(1) + 2
# # f(1) = f(0) + 1
# # f(0) = 1
# # now replace the values and add, such as f(1) = 1 + 1 is 2
# # f(2) = 2 + 2 = 4
# # f(3) = 4 + 3 = 7 // this is the total
# ######################################################

### Lambda Functions ###

my_fn = lambda x: x+1  # def my_fn(x):
#                           return x + 1
print(my_fn(3))

fn = lambda i,j: i ** j
print(fn(2,3))

