"""
new page: create and append node
forward: traverse to last valid node
backwards: traverse while prev not none
new page from back in history: create new node
Doubly linked list: 1 -> 2 -> 3 -> 4
                    1 <- 2 <- 3 <- 4
    Let's say you get to 4, and want to go back to 2, and then branch off and create a new node (browser search)
"""


class Node:

    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class Browser:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Empty Browser")
        else:
            curr_val = self.head
            while curr_val:
                print(curr_val.val, "-->", end=" ")
                curr_val = curr_val.next


b = Browser()
n1 = Node(1)
b.head = n1
n2 = Node(2)
n2.prev = n1
n1.next = n2
n3 = Node(3)
n3.prev = n2
n2.next = n3
n4 = Node(4)
n4.prev = n3
n3.next = n4
b.display()


# def display(self):
#     if self.head is None:
#         print("Empty Browser")
#     else:
#         x = self.head
#         while x:
#             print(x.val, "-->", end=" ")
#             x = x.next

