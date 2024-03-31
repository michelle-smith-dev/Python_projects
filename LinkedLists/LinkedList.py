class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val) + '->'


node1 = Node(1)
node2 = Node(2, node1)
node3 = Node(3, node2)
node4 = Node(4, node3)
node5 = Node(5, node4)
head = node5

curr_val = head
while curr_val is not None:
    print(curr_val)
    curr_val = curr_val.next

# # Traverse linked list forward and backwards; double linked list
# class Node:
#     def __init__(self, val, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev
#
#     def __repr__(self):
#         return str(self.val, self.prev) + '->'
#
#
# node1 = Node(1, next=None, prev=node2)
# node2 = Node(2, next=node1, prev=node3)
# node3 = Node(3, next=node2, prev=node4)
# node4 = Node(4, next=node3, prev=node5)
# node5 = Node(5, next=node4)
# head = node5
#
# curr_val = head
# while curr_val is not None:
#     print(curr_val)
#     curr_val = curr_val.next