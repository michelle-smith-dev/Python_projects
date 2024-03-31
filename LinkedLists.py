# Queue is why we use linked lists; the biggest advantage to using a linked list, is if you take off the head,
# and reassign to the next element in the queue, it keeps the array linked.
# Stacks is last in, first out, and is more efficient to use an array (list)


# class Node:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
#
#
#
#
# node3 = Node(val=1)
# node2 = Node(2, node3)
# node1 = Node(3, node2)
# head = Node(None, node1)
#
# # alternatively
# node1 = Node(3)
# node2 = Node(2)
# node3 = Node(1)
# node1.next = node2
# node2.next = node3

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Queue:
    def __init__(self, lst):
        self.head = Node(None)

        previous = self.head
        for i in lst:
            new_node = Node(i)
            previous.next = new_node
            previous = new_node

    # def popleft(self):
    #     pop = self.head.next
    #     self.head.next.next = self.head.next.next.next
    #     return pop

    def __repr__(self):
        linked_list = ''
        pointer = self.head
        while pointer is not None:
            linked_list += f'{pointer.val} -> '
            pointer = pointer.next
        return linked_list

    def elmnt(self):
        pointer2 = self.head
        while True:
            if 39 != pointer2:
                pointer2 = pointer2.append('next')
            elif 39 == pointer2:
                print('Found it!')
            else:
                break
# def append(self, data):
# new_node = node(data)
# cur = self.head
# while cur.next != None,
#    cur = cur.next
#    cur.next = new node

lst = Queue([11, 88, 24, 39, 4, 60])
# ret_node = lst.popleft()
print(lst)
print(Queue.elmnt(lst))


# class extrct_elmnt:
# def elmnt(linkedlist, val=False):
#     while True:
#         if 39 != self.head










# def test_1():
#     lst = Queue([1, 2, 3])
#     ret_node = lst.popleft()
#     assert ret_node.val == 1
#     assert lst.head.next.val == 2
#
#
# def run_all_tests():
#     test_1()
#
#
# run_all_tests()
