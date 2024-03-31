class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: [ListNode]):
        curr = head
        print(curr)
        prev = None
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        print(prev)
        return prev


s = Solution()
s.reverseList([1, 2, 3, 4, 5])
