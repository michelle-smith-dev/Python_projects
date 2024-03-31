# def main():
#     x = get_int()
#     print(f"x is {x}")
#
# def get_int():
#     while True:
#         try:
#             return int(input("What is the number x? "))
#         except ValueError:
#             pass
#
#
# main()

# class Solution:
#     def deleteNode(self, node):
#         curr = node
#         prev = None
#         while curr.next:
#             curr.val = curr.next.val
#             prev = curr
#             curr = curr.next
#         prev.next = None
#
#         return None
movies = ["Star Wars", "Ghandi", "Gone with the Wind", "Almost Famous"]
# gmovies = []
# for title in movies:
#     if title.startswith("Gha"):
#         gmovies.append(title)

gmovies = [title for title in movies if title.startswith("G")]

print(gmovies)