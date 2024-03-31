# # class List:
# #     def __init__(self, a_list):  # initialization
# #         self.a_list = a_list
# #     def append(self, val):  # method (class function
# #         self.a_list = [self.a_list] + [val]
# #
# # my_list = List([])  # instantiating this class of List
# # print(my_list)
# # my_list.append(3)
# # print(my_list)
#
# class Sim:
#     def __init__(self, sex, age, name):
#         self.sex = sex
#         self.age = age
#         self.name = name
#
#
# my_sim = Sim('Female', '39', 'Michelle')
# print(my_sim.sex, my_sim.age, my_sim.name, sep=",")
#
#
# class Node:
#     def __init__(self, val, prev, next):
#         self.val = val
#         self.prev = prev
#         self.next = next
#
#
# # linked lists
# node1 = Node(1, None, None)
# node2 = Node(2, None, None)
# node3 = Node(3, None, None)
#
# node1.next=node2
# node2.next=node3
# node2.prev=node1
# node3.prev=node2
#
#
#
# class ClassName:
#     class_variable = 'Available to any class instance.'  # class variable
#
#     def __init__(self, var=None):
#         self.instance_variable = 'Only available to this specific instance.'
#
# my_class_1 = ClassName()    # instantiated a class
# my_class_1.instance_variable = 'foo'    # modified data within our class
#
# my_class_2 = ClassName()
# my_class_2.instance_variable = 'bar'
#
# my_class_1.instance_variable == my_class_2.instance_variable
# my_class_1.class_variable == my_class_2.class_variable
#
#
#
#
class ClassName:
    def __init__(self, var=None):
        self.var = var

    def fn_or_method(self, num):
        result = num + self.var
        return result


my_class = ClassName(var=6)
my_class.fn_or_method(num=4)
