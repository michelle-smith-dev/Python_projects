# # students = [{"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
# #             {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
# #             {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
# #             {"name": "Draco", "house": "Slytherin", "patronus": None}
# # ]
# #
# # for student in students:
# #     print(student["name"], student["house"], student["patronus"], sep=", ")
# import string
#
#
# # def func(list1):
# #     char_list = []
# #     num_list = []
# #     punc_list = []
# #     ws_list = []
# #     for i in list1:
# #         if i.isalpha() is True:
# #             char_list.append(i)
# #         elif i.isdigit() is True:
# #             num_list.append(i)
# #         elif i in string.punctuation:
# #             punc_list.append(i)
# #         elif i.isspace() is True:
# #             ws_list.append(i)
# #
# #     return char_list, num_list, punc_list, ws_list
# #
# #
# # func("Some, string: 23nm7!0")
#
# import string
# def func(list1):
#     char_list = {'alphabetical': []}
#     num_list = {'numerical': []}
#     punc_list = {'punctuation': []}
#     ws_list = {'whitespace': []}
#     for i in list1:
#         if i.isalpha() is True:
#             char_list['alphabetical'].append(i)
#         elif i.isdigit() is True:
#             num_list['numerical'].append(i)
#         elif i in string.punctuation:
#             punc_list['punctuation'].append(i)
#         elif i.isspace() is True:
#             ws_list['whitespace'].append(i)
#     print(char_list, num_list, punc_list, ws_list, sep='\n')
#     return char_list, num_list, punc_list, ws_list
#
#
# func("Some, string: 23nm7!0")
#
# '''
# Implement a dictionary with name and age
# '''
# def personal(list1):
#
#     for name in list1:
#
# new_dict = {'names': ['john', 'sally', 'martha', 'frank', 'ashley'],
#             'ages': [12, 33, 25, 10, 5],
#             'locations': {'austin': ['north', 'south'], 'dallas': 'east', 'houston': ['west', 'north']}}
#
# # Complete the statement "foo = " so that it only contains North, South, East, or West, but not the city name.
# # Hint: this can be done using a dictionary method.
#
# foo = new_dict['locations'].values()
# print(foo)
# # print(list(foo) == [['north', 'south'], 'east', ['west', 'north']])

# list1 = [1, 2, 4]
# list2 = [1, 3, 4]
#
# for i in list2:
#     list1.append(i)
# list1.sort()
# print(list1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#         self.head = None
#
#
#     def middleNode(self):
#         curr = self.head
#         lngth = 0
#         while curr is not None:
#             lngth += 1
#             curr = curr.next
#
#
import random

y = random.randint(0, 3)
u = random.sample(range(0, 1000), 2)
print(u)
