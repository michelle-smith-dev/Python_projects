# Graph Traversal
#
#         4n
#     2n       6n
#
# 1n      3n 5n   7n
# graph = {'4': ['2', '6'],
#          '2': ['1', '3'],
#          '1': [],
#          '3': [],
#          '6': ['5', '7'],
#          '5': [],
#          '7': []}

# write a node class,
# create a binary graph node, copy and paste into bard
# using this node class, create some example graphs for me
# graph with 2 children to practice graph traversal in python

# def fn(node):
#     if node is None:
#         return None
#
#     fn(node.left)
#
#     fn(node.right)
#
# fn(4)
#
# pre order
# print(val)
# recurse(left)
# recurse(right)
#
# post order
# recurse(left)
# recurse(right)
# print(val)
#
# in order
# recurse(left)
# print(val)
# recurse(right)


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


node4 = Node(4)
node6 = Node(6)
node2 = Node(2)
node1 = Node(1)
node3 = Node(3)
node5 = Node(5)
node4.right = node6
node4.left = node2
node2.left = node4
node2.right = node3
node6.left = node5
head = node4


def graph(val):
    # go all the way down one side, back up and down the other side
    dfs_node = []
    if head.left is not None:
        dfs_node.append(head.left)
    elif head.right is not None:
        dfs_node.append(head.right)

    print(dfs_node)


graph(head)

# traverse the above graph with DFS and BFS, iteratively
# write pre/in/post using recursive to traverse the above
# level order later
