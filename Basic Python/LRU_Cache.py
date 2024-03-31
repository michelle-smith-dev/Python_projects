class LRUCache:

    def __init__(self, capacity: int):
        self.hmap = dict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.hmap:  # self.hmap == self.hmap.key() of a dictionary
            return self.hmap[key][0]  #add a second parameter in the hmap of node, key:[value, node]
        return -1

    def put(self, key: int, value: int) -> None:
        # self.hmap[key] = value
        if key in self.hmap:
            self.hmap[key][0] = value  # update queue
            node = self.hmap[key][1]  # in the below comment examples, the double linked list is [1, 2, 3, 4, tail]
            node.prev.next = node.next  # node.prev = 1, node.next = 3
            node.next.prev = node.prev  # node.next = 3, node.prev = 1
            node.prev = tail.prev  # reassign 2 to tail's prev, which is 4
            node.next = tail  # assign 2's next to tail
            tail.prev.next = node  # reassign tail's prev which is 4 to 2
            tail.prev = node  # reassign tail's prev as node 2




'''
capacity is 2
put 1, 33
put 2, 44
put 3, 55
'''
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)