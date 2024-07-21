#  create a node class for singly linked lists

# class Node:
#
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
#         # self.prev = prev
#
#     def __repr__(self):
#         return str(self.val) + '->'
#
#
# node1 = Node(2)
# node2 = Node(4, node1)
# node3 = Node(6, node2)
# head = node3
#
# curr_val = head
# while head is not None:
#     print(head)
#     head = head.next


#  create a node class for doubly linked lists
class Node:

    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __repr__(self):
        return str(self.val)


node1 = Node(2)
node2 = Node(4, node1)
node3 = Node(6, node2)
node4 = Node(8, node3)
head = node4

curr_node = head  # 8, 6
prev_node = None
while curr_node is not None:
    print(curr_node, '->')
    print(prev_node, '<-')
    prev_node = curr_node  # 8 <- 6 <- 4
    curr_node = curr_node.next  # 8 -> 6 -> 4
