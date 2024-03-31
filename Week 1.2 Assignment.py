# # x = 4.5
# # print(type(x))
# #
# # x = 'red'
# # print(type(x))
# #
# # x = "yes"
# # print(isinstance(x, str))
# #
# # x = 7
# # print(isinstance(x, float))
#
#
# # int 3
# # float 4.3
# # bool True
# # str "Hello World"
# # noneType None
#
# # print(3, 1, 2, sep="_", end="n")
#
# # foo = 3
# # bar = 7
# # print(bar >= foo)
#
# # x = 369 % 4257
# # print(x)
#
# # // floor division
# # round down to the lowest whole number when dividing two numbers
# # x = 7 // 2
# # print(x)
#
# '''
# >
# <
# >=
# <=
# ==
# !=
# is (obj is obj = true/false)
# in (obj in collection)
# '''
#
# # not, or, and
# # boolean objects with or, true or false
# # expression, blank and blank
#
# # if True:
# #     print('a')
# # elif True:
# #     print('b')
#
# # a = 8
# # b = 4
# # if b < a:
# #     print('a')
# # elif b == a:
# #     print('b')
# # else:
# #     print('c')
#
# # a, b
#
# #control flow
# # Data = "red"
# # if Data == 'green':
# #     print("go")
# #
# # elif Data == 'yellow':
# #     print("slow down")
# #
# # else:
# #     print("stop")
#
# # if grade is 70 - 79, print "c"
# # if grade is between 80 - 89, print "b"
# # if grade is between 90 - 100, print "a"
#
# # grade = 78
# # if grade >= 90:
# #     print('a')
# # elif grade >= 80:
# #     print('b')
# # elif grade >= 70:
# #     print('c')
# # else:
# #     print('f')
#
# # lists [obj1, obj2, obj3]
# # strings 'dog', '0', 'true'
#
# # indexing, indices is 0-9, so the first position is 0
my_list = ['a', '5', 'False']
print(my_list[1])
#
# # slicing
# # start, stop, 'up to but not including'
# # start is inclusive, stop: you stop on the number after what you want included
#
a_list = [4, 6, 2, 7, 9]
print(a_list[3:5])  # can also leave the last number blank,
# # and it will take from the start and print the rest of it to the right.
#
b_list = [4, 6, 2, 7, 9]
print(b_list[:])  # this is unbound and will include all left to right
#
c_list = [4, 6, 2, 7, 9, 18, 11, 3, 5, 88, 91, 42, 32, 100]
print(c_list[9:12])
#
# # collection data types, strings, lists (mutable), tuples (immutable)
# # len(obj) is the size of an object
#
print(len(c_list))
#
# # method are class functions: list.method_name
print([1].append(3))
