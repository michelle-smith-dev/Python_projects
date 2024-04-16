# Merge sort


def mergesort(arr):
    if len(arr) < 2:
        return arr
    mid_p = len(arr) // 2  # You're getting the mid index point
    left = mergesort(arr[:mid_p])  # Then splitting up the array into the first index up to but not including the mid point index
    right = mergesort(arr[mid:])  # Taking the mid point index to the end of the index

    i, j = 0, 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
    remain = right[j:]
    if i < len(left):
        remain = left[i:]
        merged.extend(remain)

    return merged

# Undirected graph is bidirectional
# Directed Graph (Directed Acyclic Graph is 1 -> 2 -> 3)
# Self reference graph 1 -> 2 -> 3 -> back to itself

class double_linked_List_node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

# BFS: Breadth First Search (Queue)
# DFS: Depth First Search (Stack)
# pre order, post order, in order