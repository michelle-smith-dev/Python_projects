class LinkedListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class linkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, val):
        node = LinkedListNode(val)
        if self.head is None:
            self.head = node
            return

        curr = self.head
        while curr:
            if curr.next is None:
                curr.next = node
                break
            curr = curr.next

    def printLinkedList(self):
        curr = self.head
        while curr is not None:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")


ll = linkedList()
ll.printLinkedList()
ll.insert(4)
ll.printLinkedList()
ll.insert(6)
ll.printLinkedList()
ll.insert(22)
ll.printLinkedList()
