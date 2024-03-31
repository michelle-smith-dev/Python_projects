debug = False
list1 = [5, 3, 8, 4, 6]
l = len(list1)


def bubble_sort(lst):
    l = len(lst)
    for i in range(len(lst)):
        for j in range(l-1):
            if debug: print(lst[j+1])
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


bubble_sort(list1)
print(list1)
# Driver code to test above
# if __name__ == "__main__":
#     lst = [64, 34, 25, 12, 22, 11, 90]
#
#     bubble_sort(lst)
#
#     print("Sorted array:")
#     for i in range(len(lst)):
#         print("%d" % lst[i], end=" ")

